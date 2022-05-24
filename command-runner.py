#Note that before running this script, you need to create a folder called "output" in the same directory that you intend to run this from.
#Note2 please edit the "devices" file to match your devices.
#Note3 please edit the "vars.py" file and adjust your credentials etc

from netmiko import ConnectHandler
import io
import time
import getpass
import vars
import os
from pyfiglet import Figlet

company = vars.company
usern = vars.username
password = vars.password
secret = vars.secret
pt = vars.port
device = vars.devicetype

localtime = time.localtime()
formattime = time.strftime("%d-%m-%Y %H:%M:%S", localtime)
datetime = time.strftime("%d-%m-%Y", localtime)


f = Figlet(font="standard", width=90)
print (f.renderText(company + " Command Runner"))
print ("Select mode, s = show/run, c = configuration or v = verification commands:")
mode = input()

devices = dict()

if mode == "s":
	print("Enter command to run on all devices:")
	command = input()

if mode == "c":
	print("Enter configuration commands with care. When finished press Ctrl-D (Ctrl-Z on Windows) once to break then please wait.")
	cmdset = []
	while True:
		try:
			cmdline = input()
		except EOFError:
			break
		cmdset.append(cmdline)

if mode == "v":
	print("Enter configuration to verify existence on all devices:")
	command = input()

if not os.path.exists("output"):
	os.mkdir("output")
if not os.path.exists("output/command-runner"):
	os.mkdir("output/command-runner")

file = open("devices","r")
for line in file:
	devices.update({line.split(",")[0]:line.split(",")[1]})


for dev_name, dev_address in devices.items():
	try:
		sw = {
			'device_type': device,
			'ip':   dev_address.strip(),
			'username': usern,
			'password': password,
			'secret': secret,
			'port' : pt,
			'verbose': False
		}
		net_connect = ConnectHandler(**sw)
		net_connect.enable()
		if mode == "c":
			output = net_connect.send_command('term len 0')
			output = net_connect.send_config_set(cmdset)
			print("\r\n##################\r\nConfiguration sent to " + dev_name + ":\r\n" + output + "\r\n##################\r\n")
		if mode == "s":
			output = net_connect.send_command('term len 0')
			output = net_connect.send_command(command)
			fi = open(os.path.join("output/command-runner/cli output " + dev_name + " " + command.replace(" ","_") + " " + formattime + ".txt"), "w")
			fi.write("\r\n##################\r\n" + dev_name + "\r\n" + command + "\r\n##################\r\n" + "\r\n" + output)
			fi.close()
			print("\r\n##################\r\n" + dev_name + "\r\n" + command + "\r\n##################\r\n" + "\r\n" + output)	
		if mode == "v":
			output = net_connect.send_command('term len 0')
			output = net_connect.send_command('show run')
			print("\r\n##################\r\nChecking " + dev_name + " running configuration contains: " + command + "\r\n")
			if command in output:
				print(" - Exists!\r\n##################\r\n")
				fi = open(os.path.join("output/command-runner/cli verify " + command.replace(" ","_") + " " + datetime + ".txt"), "a")
				fi.write("\r\n##################\r\n" + dev_name + "\r\n" + command + " - Exists!\r\n##################\r\n")
				fi.close()
			else:
				print(" - Does not exist!\r\n##################\r\n")
				fi = open(os.path.join("output/command-runner/cli verify " + command.replace(" ","_") + " " + datetime + ".txt"), "a")
				fi.write("\r\n##################\r\n" + dev_name + "\r\n" + command + " - Does not exist!\r\n##################\r\n")
				fi.close()
		net_connect.disconnect()
	except:
		if mode == "c":
			fi = open(os.path.join("output/command-runner/FAILED CONFIG DEVICES " + datetime + ".txt"), "a")
			fi.write("\r\n##################\r\nFAILED at " + formattime + " on device: " + dev_name + "\r\nConfiguration attempted:\r\n" + output + "\r\nCheck ssh access to: " + dev_address)
			fi.close()
			print("\r\n##################\r\n" + "!!!! " + dev_name + " is unreachable !!!!\r\nCheck SSH access to: " + dev_address + "##################\r\n")

		if mode == "s":
			fi = open(os.path.join("output/command-runner/FAILED DEVICES " + command.replace(" ","_") + " " + datetime + ".txt"), "a")
			fi.write("\r\n##################\r\nFAILED at " + formattime + " on device: " + dev_name + "\r\nCheck ssh access to: " + dev_address)
			fi.close()
			print("\r\n##################\r\n" + "!!!! " + dev_name + " is unreachable !!!!\r\nCheck SSH access to: " + dev_address + "##################\r\n")
			
		if mode == "v":
			fi = open(os.path.join("output/command-runner/FAILED VERIFY DEVICES " + command.replace(" ","_") + " " + datetime + ".txt"), "a")
			fi.write("\r\n##################\r\nFAILED at " + formattime + " on device: " + dev_name + "\r\nCheck ssh access to: " + dev_address)
			fi.close()
			print("\r\n##################\r\n" + "!!!! " + dev_name + " is unreachable !!!!\r\nCheck SSH access to: " + dev_address + "##################\r\n")

		continue

if(mode == "s"):
	print("\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\nShow/run command sent to all devices in list. Outputs have been saved to the output folder. Press enter to quit.\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\n")
if(mode == "c"):
	print("\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\nConfiguration commands have been sent to all devices in list. Please verify if successful. Press enter to quit.\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\n")
if(mode == "v"):
	print("\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\nVerification of command sent to all devices in list is completed. Please review the results. Press enter to quit.\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\n")
input()
