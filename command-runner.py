#Note that before running this script, you need to create a folder called "output" in the same directory that you intend to run this from.
#Note2 please edit the "devices" file to match your devices.
#Note3 please edit the "vars.py" file and adjust your credentials etc

from netmiko import ConnectHandler
import io
import datetime
import time 
import getpass
import vars
from pyfiglet import Figlet

company = vars.company
usern = vars.username
password = vars.password
secret = vars.secret
pt = vars.port



f = Figlet(font="standard", width=90)
print (f.renderText(company + " Command Runner"))

devices = dict()
print("Enter command to run on all devices:")
command = input()



file = open("devices","r")
for line in file:
	devices.update({line.split(",")[0]:line.split(",")[1]})


for dev_name, dev_address in devices.items():
	try:
		sw = {
			'device_type': 'cisco_ios',
			'ip':   dev_address.strip(),
			'username': usern,
			'password': password,
			'secret': secret,
			'port' : pt,
			'verbose': False
		}
		net_connect = ConnectHandler(**sw)
		net_connect.enable()
		output = net_connect.send_command('term len 0')
		output = net_connect.send_command(command)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%d%m%Y-%H%M%S')
		dt = datetime.datetime.fromtimestamp(ts).strftime('%d%m%Y')
		fi = open("output/cli-output-" + dev_name + "-" +command.replace(" ","_") +"-"+st+".txt", "w")
		fi.write("\r\n##################\r\n" + dev_name + "\r\n" + command + "\r\n##################\r\n" + "\r\n" + output)
		fi.close()
		print("\r\n##################\r\n" + dev_name + "\r\n" + command + "\r\n##################\r\n" + "\r\n" + output)
		net_connect.disconnect()
	except:
		fi = open("output/FAILED DEVICES" + "-" +command.replace(" ","_") + "-" + dt + ".txt", "a")
		fi.write("\r\n##################\r\nFAILED at " + st + " on device: " + dev_name + "\r\nCheck ssh access to: " + dev_address)
		fi.close()
		print("\r\n##################\r\n" + "!!!! " + dev_name + " is unreachable !!!!\r\nCheck SSH access to: " + dev_address + "##################\r\n" + "\r\n")

		continue

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\nCompleted\r\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")	
input()
