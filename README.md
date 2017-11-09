# What-s-attached-to-switch-walk-though
Define a switch and where the ARP table is and this will give you a walk though on the switch

in pull_these.csv column A put the IP of the switch you want to check out
in column B put the IP of the device with the ARP table

run "walk_though(Run this one).py" and it will prompt for your username/password

It will create a the file "output.xlsx" each sheet will be a device from column A of pull_these.csv.
"output.xlsx" Column A is the interface
Column B is the IP address
Column C is a guess as to what it is
Column D the program does an NSlookup on the IP and puts the hostname there
Column E is the mac address

Example:
FastEthernet3/0/36	172.16.16.6	Phone	phone.fake_name.com	00:1B:4F:20:60:1C

The Column C is made with the files from the OUIs folder:  Each file is named what the guess will be.  The files are a list of OUIs just like this exert from the PCs file:
3c97.0e
54ee.75
f0de.f1
If the mac address from the interface has the IOU 54ee.75 in it the guess will be "PCs"

To add an OUI to the list just open the file and put in your new OUI.

To add a new guess type just add a new file, name it what you want the guess to be, and put your OUIs in.

It should be easy :-D

