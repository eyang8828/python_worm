
############################################
# This file gives function getifip() which
# you can use to learn the IP address of the
# first interface whose IP is not 127.0.0.1
# IMPORTANT: you need to run pip install
# netifaces for this to work.
############################################

# The necessary files
# import socket, fcntl, struct
from cgi import print_arguments
import netifaces

#############################################
# Retrieves the ip of the network card with
# an IPv4 address that is not 127.0.0.1.
# @return - the string containing the IP
# address of the network adapter that is not
# if the IP is not 127.0.0.1; returns None
# if no such interface is detected
##############################################
def getifip():

	# Get all the network interfaces on the system
	networkInterfaces = netifaces.interfaces()

	# The IP address
	ipAddr = None

	print(netifaces.gateways())

	# Go through all the interfaces
	for netFace in networkInterfaces:
		
		# The IP address of the interface
		# ports = list(netifaces.ifaddresses(netFace).keys())
		# ifad = netifaces.ifaddresses(netFace)
		# addr = ifad[netifaces.AF_INET][0]['addr']
		ifad = netifaces.ifaddresses(netFace)
		ports = list(ifad.keys())
		addr =ifad[ports[1]][0]['addr']
	

		# Get the IP address
		if not addr == "127.0.0.1":

			# Save the IP addrss and break
			ipAddr = addr
			break

	return ipAddr

if __name__ == "__main__":
	getifip()
	exit


#print("The ip of the current system is: " + getifip("enp0s3"))
