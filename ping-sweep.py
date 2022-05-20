import os
import time
import itertools
import ipaddress
import html2text
from pyfiglet import Figlet
from subprocess import Popen, DEVNULL
from rich import print
from rich.console import Console
from rich.table import Table

CLEAR = "clear"
os.system(CLEAR)
localtime = time.localtime()
formattime = time.strftime("%d-%m-%Y %H:%M:%S", localtime)

active_list = []
inactive_list = []
p = {}

f = Figlet(font="standard", width=90)
print (f.renderText("Ping Sweeper"))
print("Please enter the network you wish to sweep...")
print("Example: 192.168.1.0/24")
subnet = input("\nEnter network: ")
print("\n")
print("Waiting for ping timeouts before reporting...\n")
network = ipaddress.ip_network(subnet)

for n in network.hosts():
    IP = str(n)
    p[IP] = Popen(['ping', '-c', '4', '-i', '0.2', IP], stdout=DEVNULL)

while p:
    for IP, proc in p.items():
        if proc.poll() is not None:
            del p[IP]
            if proc.returncode == 0:
                active_list.append(IP)
            elif proc.returncode == 1:
                inactive_list.append(IP)
            else:
                print(f"{IP} ERROR")
            break

table = Table(title="Ping Sweep Report \n" + formattime)
table.add_column("Active Hosts", justify="center", style="green")
table.add_column("Inactive Hosts", justify="center", style="red")
for (a, i) in itertools.zip_longest(active_list, inactive_list):
    table.add_row(a, i)

console = Console(record=True)
console.print(table)

if not os.path.exists("output"):
	os.mkdir("output")
if not os.path.exists("output/ping-sweep"):
	os.mkdir("output/ping-sweep")

htmloutput = console.export_html()
output = html2text.html2text(htmloutput)

fi = open("output/ping-sweep/ping sweep " + subnet.replace("/","_") + " " + formattime + ".txt", "w")
fi.write(output)
fi.close()
