from ovirtsdk.api import API
from ovirtsdk.xml import params

def stop_vm(vm_name):
   try:
      api = API(url="https://engine167.eayun.com",
                username="admin@internal",
                password="abc123",
                ca_file="ca.crt")

      vm = api.vms.get(name=vm_name)
      try:
         vm.stop()
         print "Stoped '%s'." % vm.get_name()
      except Exception as ex:
         print "Unable to stop '%s': %s" % (vm.get_name(), ex)

      api.disconnect()

   except Exception as ex:
      print "Unexpected error: %s" % ex
