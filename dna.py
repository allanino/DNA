import binascii
import csv

code = {}

# line = open("data/huff3_code.dat", "r").read().split()


csv_reader = csv.reader(open("data/huff3_code.dat", "r"))

i = 0
for line in csv_reader:
    row = line[0].split()
    try: 
        if code[row[0]]:
            print "*" * 10, row[0]
    except Exception:
        print 'fudeu'
    finally:
        code[row[0]] = row[1]
    i = i + 1

print i

# for i in range(0, len(line), 6):
#     code[line[i]] = line[i+1]

l = []
print len(code)
for s in code.keys():
    print "%s: %r" % (s, code[s])
    l.append(int(s))

print sorted(l), len(l)
print 

f = open("data/huff3.dict", "w+")
for code, key in sorted([(v,k) for k,v in code.iteritems()], key=lambda tup: int(tup[1])):
    f.write("%s,%s\n" %  (key,code))
# for i in range(0,257):
#     print "%d: %r" % (i, code[str(i)])

# with open("MLK_excerpt_VBR_45-85.mp3", "rb") as f:
#     byte = f.read(1)
#     for i in range(1,100):
#         print "%r" %  binascii.hexlify(byte), 
#         print "%r" %  int(binascii.hexlify(byte), 16)
#         byte = f.read(1)

