from name_work import *
from common_functions import *


def read_in_mac_table(interfaces,sh_mac_table_file):
	mac_table = read_doc (sh_mac_table_file)
	for line in mac_table:
		mac = get_mac (line)
		if len(mac) == 0:
			continue
		#print (len(line))
		#print (line)
		#print (len(line))
		if "igmp" in line:
			#print ("Kill this")
			continue	
		#print (mac)
		mac = mac[0]
		#print (len(line))
		#print (line)
		#print (type(line))		
		
		int = line.split(" ")
		int = int[-1]
		#print (int)
		int = int.lstrip(" ")
		int = int.rstrip("\n")

		int = normalize_interface_names(int)
		#print (mac)
		#print (int)
		for interface in interfaces:
		#	print (int +" "+ interface['name'] )
			if int == interface['name']:
				#print ("IT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKEDIT WORKED")
				if 'mac_addresses' in interface:
					if type(mac) is list:
						for each in mac:
							if each not in interface['mac_addresses']:
								interface['mac_addresses'].append(each)
					else:
						if mac not in interface['mac_addresses']:
							interface['mac_addresses'].append(mac)
				if 'mac_addresses' not in interface:
					if type(mac) is list:
						interface['mac_addresses'] = []
						for each in mac:
							if each not in interface['mac_addresses']:
								interface['mac_addresses'].append(each)
					else:
						mac = [mac]
						#print (mac)
						interface['mac_addresses']=mac
			if "port_channel" in interface:
				if int == interface['port_channel']:
					if 'mac_addresses' in interface:
						if type(mac) is list:
							for each in mac:
								interface['mac_addresses'].append(each)
						else:
							if mac not in interface['mac_addresses']:
								interface['mac_addresses'].append(mac)
					if 'mac_addresses' not in interface:
						if type(mac) is list:
							interface['mac_addresses'] = []
							for each in mac:
								if each not in interface['mac_addresses']:
									interface['mac_addresses'].append(each)
						else:
							mac = [mac]
							#print (mac)
							interface['mac_addresses']=mac
				
	return interfaces


def add_ips_to_int(mac_address,interface,arp_table):
	#print (interface['name'])
	unknown_mac = []
	for mac_add in mac_address:
		try:
			new_ips =  arp_table[mac_address]
		except:
			unknown_mac.append (mac_add)		
	if "ips" in interface:
		try:
			for ip in new_ips:
				interface["ips"].append(ip)
		except:
			pass
	else:
		try:
			interface["ips"] = new_ips
		except:
			pass
	if len(unknown_mac) != 0:
		if "unknown_mac" in interface:
			interface["unknown_mac"].append(unknown_mac)
		if "unknown_mac" not in interface:
			interface["unknown_mac"] = unknown_mac	
	return interface

	
def merge_interfaces_and_ips(interfaces,sh_arp_file):
	done_interfaces = []
	arp = read_doc(sh_arp_file)
	arp_table = {}
	for line in arp:
		#print (line)
		#print (len(line))
		if len(line) == 1:
			continue
		if 'INCOMPLETE' in line:
			continue
		ip = get_ip (line)[0]
		mac = get_mac (line)[0]
		if mac not in arp_table:
			arp_table[mac] = [ip]
		else:
			arp_table[mac].append(ip)
	print ("ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ARP TABLE BUILT ")
	for interface in interfaces:
		#print (interface["name"])
		if 'mac_addresses' in interface:
			#print (interface['mac_addresses'])
			for mac_address in interface['mac_addresses']:
				if type(mac_address) == list:
					for mac_add in mac_address:
						interface = add_ips_to_int(mac_add,interface,arp_table)
						#print (interface)
						
				else:
					interface = add_ips_to_int(mac_address,interface,arp_table)
					#print (interface)
			
					
	return interfaces
				
					
					
			
		