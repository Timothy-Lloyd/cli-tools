CLI-Tools*
Collection of simple CLI tools designed to be used on network devices such as routers, switches, firewalls etc.

Requirements:
python3
python3-netmiko
python3-pyfiglet
python3-rich
html2text

Prerequisites:
Create folder in the cli-tools folder called "output" - this is where applications store output.

-command-runner*
Command Runner will connect to devices listed within devices.txt and perform cli commands requested when running the program. Output will be printed to the screen and also to a file in folder called "output", assuming it is created prior to running the program.
How to use:
Edit the hosts file with the list of devices and save in the format required by the application. E.G. SW1, 192.168.1.1
Edit the vars.py file with your credentials.
Once the hosts and vars files are complete, simply run the application, pick show, configuration or verification mode and it will ask for the command(s) to be entered and then attempt to perform the tasks on each line in the hosts file.

-ping-sweeper*
Ping Sweeper will ping the subnet entered and report back with hosts which respond to the ping request. Running a ping sweep will report output to screen and also to a file Command Runner will connect to devices listed within devices.txt and perform cli commands requested when running the program. Output will be printed to the screen and also to a file in folder called "output", assuming it is created prior to running the program. Note that some hosts do not respond to ping.
How to use:
Simply run the application and enter the subnet to sweep. Maintain subnet boundaires by typeing the network address for the subnet, for example:
192.168.1.0/24 - Correct
192.168.1.1/24 - Incorrect - application will fail

*Originally forked from various sources but I have used and tweaked for so long I cannot recall.
