CLI-Tools*
Collection of simple CLI tools designed to be used on network devices such as routers, switches, firewalls etc.

Requirements:
python3
python3-netmiko
python3-pyfiglet
python3-rich

-command-runner*
Command Runner will connect to devices listed within devices.txt and perform cli commands requested when running the program. Output will be printed to the screen and also to a folder called "Output" assuming it is created prior to running the program.
How to use:
Create folder in the cli-tools folder called "output" - this is where applications store output.
Edit the hosts file with the list of devices which are to have the single command entered and save in the format required by the application. E.G. SW1, 192.168.1.1
Edit the vars.py file with your credentials.
Once the hosts and vars files are complete, simply run the application, it will ask for the command to be entered and then attempt to perform this on each line in the hosts file.

-ping-sweeper*
Ping Sweeper will ping the subnet entered and report back with hosts which respond to the ping request. Note that some hosts do not respond to ping.
How to use:
Simply run the application and enter the subnet to sweep.

*Originally forked from various sources but I have used and tweaked for so long I cannot recall.
