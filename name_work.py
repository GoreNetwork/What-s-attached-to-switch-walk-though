import re
from common_functions import *


def normalize_sh_int_status(show_int_status_file):
	doc_dict = read_doc (show_int_status_file)
	
	normalized_sh_int_status = []
	for line in doc_dict: 
		try:
			#print (line)
			tmp_line = normalize_interface_names(line)
			normalized_sh_int_status.append(tmp_line)	
		except:
			pass

		
		
	return normalized_sh_int_status

def modified_for_chassis_read_doc (file_name):
	doc = []
	for line in open(file_name, 'r').readlines():
		if "PID" in line:
			line = "  "+ line
		doc.append(line)
	return doc



def split_interface(interface):
	if re.search('\d',interface) == None:
		return [interface,'']
	num_index = interface.index(next(x for x in interface if x.isdigit()))
	str_part = interface[:num_index]
	num_part = interface[num_index:]
	return [str_part,num_part]

def normalize_interface_names(non_norm_int):
	print (non_norm_int)
	if non_norm_int == "Switch":
		return non_norm_int
	tmp = split_interface(non_norm_int)
	interface_type = tmp[0]
	port = tmp[1]
	for int_types in interfaces:
		for names in int_types:
			for name in names:
				if interface_type in name:
					return_this = int_types[1]+port
					return return_this
	return "normalize_interface_names Failed"
			
sfps = [

	[["1000BaseSX"],"GLC-SX-MMD"],
	[["1000BaseLX"],"GLC-LH-SMD"],
	[["10/100BaseTX","10/100/1000-TX"],"GLC-T"],
	[[1],"GLC-GE-100FX"],
	[[1],"SFP-10G-SR"],
	[[1],"SFP-10G-LR"],
]
#Order matters: A Nexus Ethernet would match FastEthernet,GigabitEthernet, etc, same as Gi would match Te
interfaces = [
	[["Ethernet","Eth"],"Ethernet"],
	[["FastEthernet"," FastEthernet","Fa","interface FastEthernet"],"FastEthernet"],
	[["GigabitEthernet","Gi"," GigabitEthernet","interface GigabitEthernet"],"GigabitEthernet"],
	[["TenGigabitEthernet","Te"],"TenGigabitEthernet"],
	[["Port-channel","Po"],"Port-channel"],
	[["Serial","Ser"],"Serial"],
	[["Vlan"],"Vlan"],
	[["CPU"],"CPU"],
]
