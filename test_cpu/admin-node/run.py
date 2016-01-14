# _*_ coding:utf-8 _*_

import os
import time
from vm_cpu_with_thread import *
from start_vm import *
from stop_vm import *

def test_hosts(host_ip):
   os.system('ssh helen@' + host_ip + ' ' + '\'cd /home/helen/workspace/test_cpu_script && /bin/sh pretest.sh\'')

def start_test_close(vmIpList, host_ip):
   """vmIpdicts 是字典，key 是 vm_ip，value 是 vm_name"""
   start_vm(vmIpList[1], host_ip)
   time.sleep(100)
   os.system('ssh helen@' + vmIpList[0] + ' ' + '\'cd /home/helen/workspace/test_cpu_script && /bin/sh pretest.sh\'')
   time.sleep(100)
   stop_vm(vmIpList[1])
   time.sleep(100)

def scpTestResult(ipInfo):
   os.system('scp root@' + ipInfo[0] + ':/home/helen/workspace/test_cpu_script/' + ipInfo[1] + ' .')

# 主机开启，四台虚拟机均是关闭状态才对

hostIpList = []
vmIpList = []
nfs_based = [['192.168.9.168', 'nfs_host.txt'], ['192.168.9.80', 'nfs_vm1.txt'], ['192.168.9.85', 'nfs_vm2.txt']]
local_based = [['192.168.9.81', 'local_host.txt'], ['192.168.9.82', 'local_vm1.txt'], ['192.168.9.83', 'local_vm2.txt']]
machine_info = [nfs_based, local_based]
# 对主机进行测试
for i in machine_info:
   for j in i:
      if 'host' in j[1]:
         test_hosts(j[0])

# 对虚拟机进行测试
for i in machine_info:
   for j in i:
      if 'host' in j[1]:
         host_ip = j[0]
   for j in i:
      vmIpList = []
      if 'vm' in j[1]:
         vmIpList.append(j[0])
         vmIpList.append(j[1][:-4])
         start_test_close(vmIpList, host_ip)

time.sleep(30)

# 开启所有的虚拟机
for i in machine_info:
   vm_name = []
   for j in i:
      if 'host' in j[1]:
         host_ip = j[0]
      elif 'vm' in j[1]:
         vm_name.append(j[1][:-4])
      else:
         print 'There is something wrong within it.'
   for vm in vm_name:
      start_vm(vm, host_ip)

time.sleep(300)
# 上传六台机器的测试结果
for i in machine_info:
   for j in i:
      scpTestResult(j)
draw_test()
