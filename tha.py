#coding=utf-8
import time
starttime = time.clock() 

from collections import defaultdict
gene = defaultdict(list)
gene_point = defaultdict(list)


from multiprocessing import Process

fh = open('final.txt','w')
fh.write('')
fh.close()  

def translate(a):
    if a == 'UUU' or a =='UUC':
        b = 'F'
    elif a == 'UUA' or a =='UUG' or a =='CUU' or a =='CUC' or a =='CUA' or a =='CUG':
        b = 'L'
    elif a == 'AUU' or a =='AUC' or a =='AUA':
        b = 'I'
    elif a == 'AUG':
        b = 'M'
    elif a == 'GUU' or a =='GUC' or a =='GUA' or a =='GUG':
        b = 'V'
    elif a == 'UCU' or a =='UCC' or a =='UCA' or a =='UCG':
        b = 'S'
    elif a == 'CCU' or a =='CCC' or a =='CCA' or a =='CCG':
        b = 'P'
    elif a == 'ACU' or a =='ACC' or a =='ACA' or a =='ACG':
        b = 'T'
    elif a[:2] == 'GC':
        b = 'A'
    elif a == 'UAU' or a =='UAC':
        b = 'Y'
    elif a == 'UAA':
        b = 'ochre'
    elif a == 'UAG':
        b = 'amber'
    elif a == 'CAU' or a =='CAC':
        b = 'H'
    elif a == 'CAA' or a =='CAG':
        b = 'Q'
    elif a == 'AAU' or a =='AAC':
        b = 'N'
    elif a == 'AAA' or a =='AAG':
        b = 'K'
    elif a == 'GAU' or a =='GAC':
        b = 'D'
    elif a == 'GAA' or a =='GAG':
        b = 'E'
    elif a == 'UGU' or a =='UGC':
        b = 'C'
    elif a == 'UGA':
        b = 'opal'
    elif a == 'UGG':
        b = 'W'
    elif a[:2] == 'CG' or a == 'AGA' or a== 'AGG':
        b = 'R'
    elif a == 'AGU' or a == 'AGC':
        b = 'S'
    elif a[:2] == 'GG':
        b = 'G'
    else:
        b = 'none'
    return b
'''
RNA到蛋白质的替换规则
'''


fh_2 = open('chr1.fasta','r')
all_base = str(fh_2.read())
all_base = all_base.replace('\n','')
all_base = all_base[5:]  #整个读取fasta

fh_1 = open('Chr1.gff','r')

while 1:
    line = fh_1.readline()
    if not line: 
        break
    tab = line.split()
    if 'CDS' in tab[2]:
        seq = all_base[int(tab[3]):int(tab[4])+1]
        #seq = seq[int(tab[7]):]
        if tab[6] == '-':
            seq = seq[::-1] #因为实在懒得翻文档，直接用最傻逼的办法手动翻转DNA链
            seq = seq.replace('A','U')
            seq = seq.replace('T','A')
            seq = seq.replace('U','T')
            seq = seq.replace('C','U')
            seq = seq.replace('G','C')
            seq = seq.replace('U','G')  
        name = tab[8].split(',')[0]
        name = name[7:]
        gene[name].extend(seq)
'''
for key in gene:
    if len(gene[key]) % 3 !=0:
        print key
'''
fh_1.close()     

for key in gene:
    for i in range(0,len(gene[key]),3):
        seq = gene[key][i:i+3]
        gene_seq = ''.join(seq)
        gene_seq = gene_seq.replace('T','U')
        gene_point[str(key)].extend([gene_seq])

end = defaultdict(str)

for key in gene_point:
    tab = []
    for i in gene_point[key]:
        result = translate(i)
        if result == 'amber' or result == 'ochre' or result == 'opal' or result == 'none': 
            break
        tab = tab + [result]  #翻译成蛋白质，遇到终止子跳出，不过cds一般不可能有终止子
    final = ''.join(tab)
    end[key] = final
'''
values=set()
for key in end.keys():
    val = end[key]
    if val in values: 
        if key[]
            del end[key]
    else:
        values.add(val)

    #去除重复项，后来考虑到可能多个基因编码同一个蛋白质，于是注释掉了
'''
'''
for key in end:
    if end[key][0] != 'M':
        print key
'''
fh = open('final.txt','a')
for key in end:
    fh.write('>'+ str(key)+'\n')
    fh.write(end[key]+'\n')

fh.close()

endtime = time.clock() 
print 'Totally spend' + str((endtime - starttime)) + 'seconds'  


'''
下面是这个脚本的第一版，已经没用了，仅供参考

for key in gene:
    for i in gene[key]:
        seq_start = int(gene[key][0])
        seq_end = int(gene[key][1])+1
        gene_seq = all_base[seq_start:seq_end] #你感受一下，你随便感受一下，在整个fasta里面找对应序列……太可怕了

        if gene[key][2] is '-':
            seq = gene_seq
            seq = seq[::-1] #翻转dna链
            seq = seq.replace('A','U')
            seq = seq.replace('T','A')
            seq = seq.replace('U','T')
            seq = seq.replace('C','U')
            seq = seq.replace('G','C')
            seq = seq.replace('U','G')   
            gene_seq = seq
        seq = gene_seq  
        gene_seq = gene_seq.replace('T','U') #转录成mrna
        
        for i in range(0,len(gene_seq),3):
            seq = gene_seq[i:i+3]
            gene_point[str(key)].extend([seq]) #把rna拆分为三个一组

endtime3 = time.clock() 
print 'Totally spend' + str((endtime3 - endtime2)) + 'seconds'  #测试时间，正式版代码中请注释掉这一块

gene = defaultdict(str)

for key in gene_point:
    tab = []
    for i in gene_point[key]:
        result = translate(i)
        if result == 'amber' or result == 'ochre' or result == 'opal' or result == 'none': 
            break
        tab = tab + [result]  #翻译成蛋白质，遇到终止子跳出
    final = ''.join(tab)
    gene[key] = final

endtime4 = time.clock() 
print 'Totally spend' + str((endtime4 - endtime3)) + 'seconds'  #测试时间，正式版代码中请注释掉这一块

fh = open('final.txt','a')
for key in gene:
    fh.write('>'+ str(key)+'\n')
    fh.write(gene[key]+'\n')

endtime5 = time.clock() 
print 'Totally spend' + str((endtime5 - endtime4)) + 'seconds'  #测试时间，正式版代码中请注释掉这一块


endtime = time.clock() 
print 'Totally spend' + str((endtime - starttime)) + 'seconds'  

'''

    

       





    
        
























