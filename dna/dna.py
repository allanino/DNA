import binascii
import csv

class DNA(object):
    """
    This class implements two main methods:
        encode(file): encodes a arbitrary file in DNA form as described
                      in Nature article.
        decode(file): decode file from DNA.
    """
    # Huffman code dictionary
    code = {}

    def __init__(self):
        """ Populates the Huffman code dictionary """

        csv_reader = csv.reader(open("data/huff3.dict", "r"), delimiter=',')
        for row in csv_reader:
            self.code[row[0]] = row[1]

    def __S0toS1(file):
        pass




if __name__ == '__main__':
    dna = DNA()
    code = dna.code

    for s in code.keys():
        print "%s: %r" % (s, code[s])
