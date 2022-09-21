
infile = open('sometext.txt', 'r')

d = {}

for rec in infile:
    rec = rec.strip()
    rec = rec.lower()
    words = rec.split()

for word in words:
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1

print('Word,Frequency')

for key in d:
    print(str(key) + ',' + str(d[key]))

infile.close()