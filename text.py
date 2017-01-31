fh = open('chr1_pep.txt','r')
fh2 = open('answer.txt','w')
fh2.write('')
fh2.close()

fh2 = open('answer.txt','a')

while 1:
    line = fh.readline()
    if not line:
        break
    line = line.split()
    line = str(line[0])
    if line[0] is '>':
        line = line[:13]
        fh2.write('\n'+line+'\n')
    else:
        fh2.write(line)

fh = open('answer.txt','r')
file = fh.read()
file = file[1:]

fh = open('answer.txt','w')
fh.write(file)

'''
fh = open('answer.txt','r')
allseq = fh.read()
allseq = str(allseq)
seq = seq.repalace('<',)
'''
fh.close()
fh2.close()