# _*_ coding: utf-8 _*_

import os
from time import sleep

# 输入 5，返回 '0,1,2,3,4,5'
def returnNumList(num):
   s = ''
   for i in range(num + 1):
      s += str(i)
   s = ','.join(s)
   return s

cpu_num = int(os.popen('cat /proc/cpuinfo | grep \'processor\' | wc -l').readline())

for n in range(cpu_num):
   s = returnNumList(n)   
   os.system('taskset -c ' + s + ' sysbench --test=cpu --cpu-max-prime=10 run > ./a.txt')
   with open("./a.txt", 'r') as f:
      linesList = f.readlines()
   linesListNew = [(''.join(line.strip().split(' '))).split(':') for line in linesList]
   for index, value in enumerate(linesListNew):
      if len(value) == 2:
         if value[0] == 'totaltime':
   	      run_time = float(value[1][:-2])
   record = s + ' ' + str(run_time)
   with open("./nfs_vm1.txt", 'a') as f1:
      if int(n) == 0:
         f1.write('测试对象 基于nfs的虚拟机（1cpu8核）\n')
      f1.write(record + '\n')

   sleep(8)
