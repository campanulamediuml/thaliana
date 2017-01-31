#coding=utf-8
from collections import defaultdict
gene1 = defaultdict(str)
gene2 = defaultdict(str)

fh1 = open('answer.txt')
fh2 = open('final.txt')
fh3 = open('compare.txt','w')
fh3.write('')
fh3.close()
fh3 = open('compare.txt','a')

count = 0
while 1:
    line = fh1.readline()
    if not line:
        break
    count = count + 1
    if count % 2 !=0:
        name = line
        continue
    gene1[name] = line

fh3.write('标准答案中出现下列重复基因：'+'\n')
c=0
values=set()
for key in gene1.keys():
    val = gene1[key]
    if val in values:
        fh3.write(str(key))
        c=c+1
    else:
        values.add(val)
fh3.write('总计'+str(c)+'个'+'\n')

while 1:
    line = fh2.readline()
    if not line:
        break
    count = count + 1
    if count % 2 !=0:
        name = line
        continue
    gene2[name] = line

fh1.close()
fh2.close()

tab1 = []
for key in gene1:
    tab1 = tab1 + [gene1[key]]

fh3.write('标准答案中共有序列：'+str(len(tab1))+'\n')

tab2 = []
for key in gene2:
    tab2 = tab2 + [gene2[key]]

fh3.write('脚本答案中共有序列：'+str(len(tab2))+'\n')

fh3.write('下列基因存在于gff，但是在标准答案中缺失'+'\n')
c=0
for key in gene2:
    if key not in gene1:
        fh3.write(str(key))
        c=c+1
fh3.write('总计'+str(c)+'个'+'\n')

fh3.write('下列基因存在于标准答案，但是没正确通过脚本找到'+'\n')
c=0
for key in gene1:
    if key not in gene2:
        fh3.write(str(key))
        c=c+1
        
fh3.write('总计'+str(c)+'个'+'\n')

fh3.write('下列基因脚本提供的答案和标准答案序列存在差异'+'\n')
n=0
for key in gene1:
    if gene1[key] != gene2[key]:
        fh3.write(str(key))
        n=n+1
fh3.write('总计'+str(n)+'个'+'\n')



