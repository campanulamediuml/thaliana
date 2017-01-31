#coding=utf-8
import os
import time
os.system('unzip chr1.fasta.zip')
print '开始处理数据...'
os.system('python tha.py')
print '数据处理完毕，开始分析CDS序列与标准答案区别'
os.system('python text.py')
time.sleep(2)
os.system('python compare.py')
print '对比完毕，访问final.txt查看答案，访问compare.txt查看答案与标准答案的区别'
raw_input('按回车键退出')
exit()
