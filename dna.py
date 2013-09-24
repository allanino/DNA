import binascii
import csv

code = {}

line = open("data/huff3_code.dat", "r").read().split()
print line

for i in range(0, 257, 6):
    code[line[i]] = line[i]

for s in code:
    print s

for i in range(0,257):
    print "%d: %s" % (i, code[str(i)])

# with open("MLK_excerpt_VBR_45-85.mp3", "rb") as f:
#     byte = f.read(1)
#     for i in range(1,100):
#         print "%r" %  binascii.hexlify(byte), 
#         print "%r" %  int(binascii.hexlify(byte), 16)
#         byte = f.read(1)