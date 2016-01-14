from ovirtsdk.api import API
from ovirtsdk.xml import params

def start_vm(vm_name, host_ip):
   try:
      api = API(url="https://engine167.eayun.com",
                username="admin@internal",
                password="abc123",
                ca_file="ca.crt")

      vm = api.vms.get(name=vm_name)
      try:
         vm.start(
               action = params.Action(
                  vm = params.VM(
                     host = params.Host(address = host_ip)
                     )
                  )
               )
         print "Started '%s'." % vm.get_name()
      except Exception as ex:
         print "Unable to start '%s': %s" % (vm.get_name(), ex)

      api.disconnect()

   except Exception as ex:
      print "Unexpected error: %s" % ex
