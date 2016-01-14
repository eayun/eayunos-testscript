#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt  
from pylab import *

def draw_test():
   fa = open("./nfs_host.txt", 'r')
   fb = open("./nfs_vm1.txt", 'r')
   fc = open("./nfs_vm2.txt", 'r')
   fd = open("./local_host.txt", 'r')
   fe = open("./local_vm1.txt", 'r')
   ff = open("./local_vm2.txt", 'r')

   linesList_a = fa.readlines()
   linesList_b = fb.readlines()
   linesList_c = fc.readlines()
   linesList_d = fd.readlines()
   linesList_e = fe.readlines()
   linesList_f = ff.readlines()

   linesList_a = [line.strip().split(" ") for line in linesList_a]
   linesList_b = [line.strip().split(" ") for line in linesList_b]
   linesList_c = [line.strip().split(" ") for line in linesList_c]
   linesList_d = [line.strip().split(" ") for line in linesList_d]
   linesList_e = [line.strip().split(" ") for line in linesList_e]
   linesList_f = [line.strip().split(" ") for line in linesList_f]

   fa.close()
   fb.close()
   fc.close()
   fd.close()
   fe.close()
   ff.close()

   a_discription = linesList_a[0][1]
   b_discription = linesList_b[0][1]
   c_discription = linesList_c[0][1]
   d_discription = linesList_d[0][1]
   e_discription = linesList_e[0][1]
   f_discription = linesList_f[0][1]

   linesList_a = linesList_a[1:]
   linesList_b = linesList_b[1:]
   linesList_c = linesList_c[1:]
   linesList_d = linesList_d[1:]
   linesList_e = linesList_e[1:]
   linesList_f = linesList_f[1:]

   def avg(List):
      sum = 0
      for a in List:
         sum += a
      avg = sum / len(List)
      print avg

   a_y = [float(item[1]) for item in linesList_a]
   avg(a_y)
   b_y = [float(item[1]) for item in linesList_b]
   avg(b_y)
   c_y = [float(item[1]) for item in linesList_c]
   avg(c_y)
   d_y = [float(item[1]) for item in linesList_d]
   avg(d_y)
   e_y = [float(item[1]) for item in linesList_e]
   avg(e_y)
   f_y = [float(item[1]) for item in linesList_f]
   avg(f_y)
   
   x = range(len(a_y))

   plt.plot(x, a_y, '-or', label=unicode(a_discription, "utf-8"))
   plt.plot(x, b_y, '-ob', label=unicode(b_discription, "utf-8"))
   plt.plot(x, c_y, '-og', label=unicode(c_discription, "utf-8"))
   plt.plot(x, d_y, '-^r', label=unicode(d_discription, "utf-8"))
   plt.plot(x, e_y, '-^b', label=unicode(e_discription, "utf-8"))
   plt.plot(x, f_y, '-^g', label=unicode(f_discription, "utf-8"))
   
   #plt.ylim(80.6, 81.3, 500000)
   plt.ylim(0.0, 1.0, 500000)

   ax = plt.gca()
   ax.set_xticks(x)
   ax.set_xticklabels(['1','2','3','4','5','6','7','8'], rotation = 45); 
   plt.xlabel(u'被测试对象')
   plt.ylabel(u'运行计算 50000 个质数所需时长，单位为秒')
   plt.title(u'测试虚拟机的 cpu 性能')
   plt.legend()
   plt.savefig('./a.png', format='png')
   plt.show()
