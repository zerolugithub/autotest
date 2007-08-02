#!/usr/bin/python
#
# Copyright 2007 Google Inc. Released under the GPL v2

"""
This module defines the Guest class in the Host hierarchy.

Implementation details:
You should import the "hosts" package instead of importing each type of host.

	Guest: a virtual machine on which you can run programs
"""

__author__ = """
mbligh@google.com (Martin J. Bligh),
poirier@google.com (Benjamin Poirier),
stutsman@google.com (Ryan Stutsman)
"""


import ssh_host


class Guest(ssh_host.SSHHost):
	"""
	This class represents a virtual machine on which you can run 
	programs.
	
	It is not the machine autoserv is running on.
	
	Implementation details:
	This is an abstract class, leaf subclasses must implement the methods
	listed here and in parent classes which have no implementation. They 
	may reimplement methods which already have an implementation. You 
	must not instantiate this class but should instantiate one of those 
	leaf subclasses.
	"""
	
	controlling_hypervisor = None

	
	def __init__(self, controlling_hypervisor):
		"""
		Construct a Guest object
		
		Args:
			controlling_hypervisor: Hypervisor object that is 
				responsible for the creation and management of 
				this guest
		"""
		hostname= controlling_hypervisor.new_guest()
		super(Guest, self).__init__(hostname)
		self.controlling_hypervisor= controlling_hypervisor

	
	def __del__(self):
		"""
		Destroy a Guest object
		"""
		self.controlling_hypervisor.delete_guest(self.hostname)

	
	def hardreset(self):
		"""
		Perform a "hardreset" of the guest.
		
		It is restarted through the hypervisor. That will restart it 
		even if the guest otherwise innaccessible through ssh.
		"""
		return self.controlling_hypervisor.reset_guest(self.hostname)

