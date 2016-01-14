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

environment = raw_input('您的虚拟化环境的 ip 地址：')
os.system('wget http://' + environment + '/ca.crt')
nfs_based = [[raw_input('基于 nfs 存储的主机的 ip 地址：'), raw_input('该台机器在虚拟平台中的名称：') + '.txt'], [raw_input('基于 nfs 存储的 1cpu8cores 的虚拟机的 ip 地址：'), raw_input('该台机器在虚拟平台中的名称：') + '.txt'], [raw_input('基于 nfs 存储的 8cpu1core 的虚拟机的 ip 地址：'), raw_input('该台机器在虚拟平台中的名称：') + '.txt']]
local_based = [[raw_input('基于本地存储的主机的 ip 地址：'), raw_input('该台机器在虚拟平台中的名称：') + '.txt'], [raw_input('基于本地存储的 1cpu8cores 的虚拟机的 ip 地址：'), raw_input('该台机器在虚拟平台中的名称：') + '.txt'], [raw_input('基于本地存储的 8cpu1core 的虚拟机的 ip 地址：'), raw_input('该台机器在虚拟平台中的名称：') + '.txt']] 
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
