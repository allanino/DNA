#!/usr/bin/python

import binascii
import csv
from random import randint
import os
import math
import zipfile
import sys
import argparse

class DNA(object):
    """
    This class implements four main methods:
        encode(file): encode an arbitrary file in DNA form as described
                      in Nature's article.
        encode_split(file): encode and prepare file for sequencing.
        decode(file): decode file from DNA.
        decode_join(file): decode splitted file.
    """
    
    # Huffman code dictionary
    code = {}

    # Dictionary with files 2-trits
    files_trits = {}

    def __init__(self):
        """ Populates the Huffman code dictionary """

        # Read the dictionary from data/huff3.dict
        # I made this file from the View_huff3.cd.new.correct
        huff_dict = open(os.path.join(os.path.dirname(__file__), "data/huff3.dict"), "r")
        csv_reader = csv.reader(huff_dict, delimiter=',')
        for row in csv_reader:
            self.code[row[0]] = row[1]

    def encode(self, input_file):
        """ Encode input_file in an DNA string """

        s1 = self.__S0_to_S1(input_file)
        s4 = self.__S1_to_S4(s1)
        s5 = self.__S4_to_S5(s4)
        open(input_file + '.dna', 'w').write(s5)

    def decode(self, input_file):
        """ Decode file in an DNA string """
        s5 = open(input_file, 'r').read()
        s4 = self.__S5_to_S4(s5)
        s0 = self.__S4_to_S0(s4)
        # Save s0 after conversion from hexadecimal to bytes
        open(input_file[:-4]+'.decoded', 'wb').write(binascii.unhexlify(s0))

    def decode_join(self, input_file):
        """ Decode and join DNA zip file into DNA string """
        Findex = self.__Files_to_Findex(input_file)
        Fi = self.__Findex_to_Fi(Findex)
        s5 = self.__Fi_to_S5(Fi)
        s4 = self.__S5_to_S4(s5)
        s0 = self.__S4_to_S0(s4)
        # Save s0 after conversion from hexadecimal to bytes
        open(input_file[:-13]+'.decoded', 'wb').write(binascii.unhexlify(s0))
        
    def encode_split(self, input_file):
        """ Encode file in many overlapping DNA string. Returns a zip file """

        s1 = self.__S0_to_S1(input_file)
        s4 = self.__S1_to_S4(s1)
        s5 = self.__S4_to_S5(s4)
        F = self.__S5_to_Fi(s5)
        Findex = self.__Fi_to_Findex(F, input_file)
        self.__Findex_to_Files(Findex, input_file)
        return Findex

    def __S0_to_S1(self, input_file):
    
        # Update 2-trits file dictionary (for later use: if more than one file)
        trit = self.__base10_to_base3(len(self.files_trits))
        trit = '0'  * (2 - len(trit)) + trit
        self.files_trits[input_file] = trit
        # Concatenate byte by byte to s1 (after Huffman codification)
        s1 = ""
        with open(input_file, 'rb') as f:
            byte = f.read(1)
            while byte:
                s1 = s1 + self.code[str(int(binascii.hexlify(byte), 16))]
                byte = f.read(1)
        return s1

    def __S1_to_S4(self, s1):

        # Compute s2
        n = len(s1)
        s2 = self.__base10_to_base3(n)
        s2 = '0' * (20 - len(s2)) + s2
        
        # Compute s3
        s3 = '0' * (-(n + len(s2) % 25) % 25)

        # Compute s4
        s4 = s1 + s3 + s2
        return s4

    def __S4_to_S5(self, s4):

        # Create table
        dna_table = {
            'A': ['C', 'G', 'T'],
            'C': ['G', 'T', 'A'],
            'G': ['T', 'A', 'C'],
            'T': ['A', 'C', 'G']
        }

        s5 = ''
        s5 = s5 + dna_table['A'][int(s4[0])]
        for c in s4[1:]:
            s5 = s5 + dna_table[s5[-1]][int(c)]

        return s5

    def __S5_to_Fi(self, s5):
        n = len(s5)
        F = []
        for i in range(0, n/25 - 3):
            # Reverse if odd
            if i % 2 == 1:
                F.append(self.__reverse_complement(s5[25*i:25*i+100]))
            else:
                F.append(s5[25*i:25*i+100])
        return F

    def __Fi_to_Findex(self, F, input_file):
        
        # Indexed segments
        Findex = []

        # File ID
        ID = self.files_trits[input_file]

        # Create table
        dna_table = {
            'A': ['C', 'G', 'T'],
            'C': ['G', 'T', 'A'],
            'G': ['T', 'A', 'C'],
            'T': ['A', 'C', 'G']
        }

        # For each segment compute the IX
        for i in range(0, len(F)):
            i3 = self.__base10_to_base3(i)
            i3 = '0' * (12 - len(i3)) + i3
            P = (int(ID[1-1]) + int(i3[1-1]) + int(i3[3-1]) +
                 int(i3[5-1]) + int(i3[7-1]) + int(i3[9-1]) + int(i3[11-1])) % 3
            IX = ID + i3 + str(P)

            ix = ''
            ix = ix + dna_table[F[i][-1]][int(IX[0])]
            for c in IX[1:]:
                ix = ix + dna_table[ix[-1]][int(c)]
 
            if F[i][0] == 'A':
                F[i] = 'T' + F[i]
            elif F[i][0] == 'T':
                F[i] = 'A' + F[i]
            else:
                if randint(0,1) == 0:
                    F[i] = 'A' + F[i]
                else:
                    F[i] = 'T' + F[i]

            if ix[-1] == 'C':
                ix = ix + 'G'
            elif ix[-1] == 'G':
                ix = ix + 'C'
            else:
                if randint(0,1) == 0:
                    ix = ix + 'G'
                else:
                    ix = ix + 'C'

            Findex.append(F[i] + ix)

        return Findex

    def __Findex_to_Files(self, Findex, input_file):
        temp_dir = input_file +'.splitted'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        zf = zipfile.ZipFile(temp_dir +'.zip', 'w', zipfile.ZIP_DEFLATED)

        # Necessary number of leading zeros
        n0 = int(math.log(len(Findex), 10) + 1)

        i = 0
        for f in Findex:
            fragment_file = "{0}.{1:0{2}d}".format(os.path.basename(input_file), i, n0) 
            open(fragment_file, 'w').write(f)
            zf.write(fragment_file)
            os.remove(fragment_file)
            i = i + 1
        os.rmdir(temp_dir)

    def __Files_to_Findex(self, input_file):
        
        # Remove the .zip
        temp_dir = input_file[:-4]

        # Extract files to temp_dir
        zipfile.ZipFile(input_file, 'r').extractall(temp_dir)

        Findex = []
        for f in os.listdir(temp_dir):
            fragment_file = temp_dir + os.sep + f
            Findex.append(open(fragment_file, 'r').read())
            os.remove(fragment_file)

        os.rmdir(temp_dir)

        return Findex

    def __Findex_to_Fi(self, Findex):

        # Create inverse table
        dna_inv_table = {
            'A': {'T': '0', 'G': '1', 'C': '2'},
            'C': {'A': '0', 'T': '1', 'G': '2'},
            'G': {'C': '0', 'A': '1', 'T': '2'},
            'T': {'G': '0', 'C': '1', 'A': '2'}
        }

        F = [''] * len(Findex)
        for Fi in Findex:

            # Check if reverse complemented
            if Fi[0] != 'T' and Fi[0] != 'A':
                Fi = self.__reverse_complement(Fi)

            # Remove prepended A/T and appended C/G
            Fi = Fi[1:116] # Prior lenght of Fi is 117
            
            # Extract ix (last 15) n DNA format
            ix = Fi[-15:]
            Fi = Fi[:-15]

            # Convert ix to trits (IX)
            lastFi = Fi[-1]
            IX = dna_inv_table[ix[0]][lastFi]
            for i in range(1, 15):
                IX = IX + dna_inv_table[ix[i]][ix[i-1]]
            
            # Extract ID
            ID = IX[:2]

            # Extract i3 and i
            i3 = IX[2:len(IX)-1]
            i = self.__base3_to_base10(i3)

            # Checksum error
            P = int(IX[-1])
            Pexpected = (int(ID[1-1]) + int(i3[1-1]) + int(i3[3-1]) + 
                         int(i3[5-1]) + int(i3[7-1]) + int(i3[9-1]) + int(i3[11-1])) % 3
            if P != Pexpected:
                print "Corrupted segment:\nID = %s\ni = %d" %(ID, i)
            else:
                # Save Fi
                if i % 2 == 1:
                    F[i] = self.__reverse_complement(Fi)
                else:
                    F[i] = Fi
        return F

    def __Fi_to_S5(self, Fi):

        # In real applications we should check if the overlapping
        # parts are equal. I won't do that for now

        s5 = Fi[0][0:75]
        for f in Fi:
            s5 = s5 + f[-25:]
        return s5

    def __S5_to_S4(self, s5):

        # Create inverse table
        dna_inv_table = {
            'A': {'T': '0', 'G': '1', 'C': '2'},
            'C': {'A': '0', 'T': '1', 'G': '2'},
            'G': {'C': '0', 'A': '1', 'T': '2'},
            'T': {'G': '0', 'C': '1', 'A': '2'}
        }

        s4 = ''
        for i in range(len(s5) -1, 0,-1):
            s4 = dna_inv_table[s5[i]][s5[i-1]] + s4
        s4 = dna_inv_table[s5[0]]['A'] + s4

        return s4

    def __S4_to_S0(self, s4):

        # s2 is the last 20 trits
        s2 = s4[-20:]

        # n = len(s1) is s2 converted to base 10 
        n = self.__base3_to_base10(s2)

        # s1 is the first n trits
        s1 = s4[:n]

        # Time to convert s1 from trits to bytes in s0
        inverted_code = dict([v,k] for k,v in self.code.items())
        s0 = ''
        i = 0
        while i != n:
            if s1[i:i+5] in inverted_code.keys():
                s0 = s0 + ''.join('%02x' % int(inverted_code[s1[i:i+5]]))
                i = i + 5
            else:
                s0 = s0 + ''.join('%02x' % int(inverted_code[s1[i:i+6]]))
                i = i + 6

        return s0

    def __base10_to_base3(self,n):
        """ Input: int and Output: str """
        if n == 0:
            return '0'

        s = ''
        while n != 0:
            s =  str((n % 3)) + s
            n = n/3
        return s

    def __base3_to_base10(self,n):
        """ Input: str and Output: int """
        n = int(n)
        if n == 0:
            return 0

        res = 0
        b = 1
        while n != 0:
            res = res + (n % 10) * b
            n = n/10
            b = 3 * b
        return res
        # return int(n , 3) <= Hahaha

    def __reverse_complement(self,s):
        reverse = ''

        complement_dict = {'A': 'T', 'T': 'A', 'C':'G', 'G': 'C'}

        for c in s:
            reverse = complement_dict[c] + reverse

        return  reverse

def main():
    parser = argparse.ArgumentParser(prog='dna')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', help='encode file and save it as .dna', action="store_true")
    group.add_argument('-s', help='encode file and save it as .splitted.zip', action="store_true")
    group.add_argument('-d', help='decode .dna file and save as .decoded', action="store_true")
    group.add_argument('-j', help='decode .splitted.zip file and save it as .decoded', action="store_true")
    parser.add_argument('file', type=str, help='File to be encoded/decoded.')
    args = parser.parse_args()
    
    dna = DNA()
    if args.e:
        dna.encode(args.file)
    elif args.s:
        dna.encode_split(args.file)
    elif args.d:
        if args.file[-4:] != '.dna':
            print "I only decode files terminated in .dna!"
            sys.exit(1)
        dna.decode(args.file)
    elif args.j:
        if args.file[-13:] != '.splitted.zip':
            print "I only decode and join files terminated in .splitted.zip!"
            sys.exit(1)
        dna.decode_join(args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()