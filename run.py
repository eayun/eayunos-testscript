# _*_ coding:utf-8 _*_

import os
import time
from vm_cpu_with_thread import *
from start_vm import *
from stop_vm import *

def test_hosts(hostIpList):
   for host_ip in hostIpList:
      os.system('ssh helen@' + host_ip + ' ' + '\'cd /home/helen/workspace/test_cpu_script && python test_cpu.py\'')

def start_test_close(vmIpList, host_ip):
   """vmIpdicts 是字典，key 是 vm_ip，value 是 vm_name"""
   start_vm(vmIpList[1], host_ip)
   time.sleep(200)
   os.system('ssh helen@' + vmIpList[0] + ' ' + '\'cd /home/helen/workspace/test_cpu_script && python test_cpu.py\'')
   time.sleep(65)
   stop_vm(vmIpList[1])
   time.sleep(10)

def scpTestResult(ipInfo):
   for info in ipInfo:
      os.system('scp root@' + info[0] + ':/home/helen/workspace/test_cpu_script/' + info[1] + ' .')

# 主机开启，四台虚拟机均是关闭状态才对

hostIpList = ['192.168.9.81', '192.168.9.168']
print '=========================================='
test_hosts(hostIpList)
time.sleep(10)
print '------------------------------------------'
# 开启 for_test 虚拟机，进行测试，关闭 for_test 虚拟机
vmIpList = ['192.168.9.82', 'for_test']
start_test_close(vmIpList, hostIpList[0])
# 开启 single_test 虚拟机，进行测试，关闭 single_test 虚拟机
vmIpList = ['192.168.9.80', 'single_test']
start_test_close(vmIpList, hostIpList[1])
# 开启 for_test_ 虚拟机，进行测试，关闭 for_test_ 虚拟机
vmIpList = ['192.168.9.83', 'for_test_']
start_test_close(vmIpList, hostIpList[0])
# 开启 single_test_ 虚拟机，进行测试；既然是最后一台就不关闭 single_test_ 虚拟机
vmIpList = ['192.168.9.85', 'single_test_']
start_test_close(vmIpList, hostIpList[1])

# 开启所有的虚拟机
vm_ip_lists = [['for_test', hostIpList[0]], ['for_test_', hostIpList[0]], ['single_test', hostIpList[1]], ['single_test_', hostIpList[1]]]
for ip in vm_ip_lists:
   start_vm(ip[0], ip[1])
time.sleep(300)
# 上传六台虚拟机的测试结果
ipInfo = [['192.168.9.80', 'nfs_vm1.txt'], ['192.168.9.81', 'local_host.txt'], ['192.168.9.82', 'local_vm1.txt'], ['192.168.9.83', 'local_vm2.txt'], ['192.168.9.85', 'nfs_vm2.txt'], ['192.168.9.168', 'nfs_host.txt']]
scpTestResult(ipInfo)
draw_test()
