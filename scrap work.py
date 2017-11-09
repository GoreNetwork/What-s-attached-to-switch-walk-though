from common_functions import *
#from pull import *
#from mac_and_arp_work import *
from napalm import get_network_driver	
from getpass import getpass
from pprint import pprint
from name_work import *
import os

def normalize_mac (mac):
	mac = mac.strip(" ")
	mac = mac.replace('.','')
	mac = mac.upper()
	t = iter(mac)
	mac = ':'.join(a+b for a,b in zip(t, t))
	return mac
	

def ouicorrect(list):
	templist = []
	for oui in list:
		templist.append(normalize_mac (oui[0:7]))
	return (templist)	
	
def check_ouis(folder_name):
	os.chdir(folder_name)
	files = os.listdir()
	#print (files)
	OUIs = {}	
	for file in files:
		q =open(file).readlines()
		fixed_oui = ouicorrect (q)
		for each_oui in fixed_oui:
			OUIs [each_oui]= file
	return OUIs
	
folder_name = "OUIs"
pprint (check_ouis(folder_name))