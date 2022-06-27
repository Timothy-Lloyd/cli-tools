# CLI-Tools*
CLI-Tools is a collection of simple CLI tools designed to be used on network devices such as routers, switches, firewalls etc.  
_*Originally forked from various sources but I have used and tweaked for so long I cannot recall._  

**To do list:**  
1. Add configuration best practice comparison tool

## Requirements (tested versions):
python3 (3.8.10)  
python3-netmiko (2.4.2)  
python3-pyfiglet  (0.8.post0)
python3-rich  (12.4.1)
html2text (2020.1.16)  

## Prerequisites:
Create folder in the cli-tools folder called "output" - this is where the tools store output.  

## command-runner*
Command Runner will connect to devices listed within devices.txt and perform cli commands requested when running the program. Output will be printed to the screen and also to a file in folder called "output", assuming it is created prior to running the program.
### How to use:
Edit the hosts file with the list of devices and save in the format required by the application. E.G. SW1, 192.168.1.1  
Edit the vars.py file with any updates.  
Once the hosts and vars files are complete, simply run the application, enter your credentials then pick show, configuration or verification mode and it will ask for the command(s) to be entered and then attempt to perform the tasks on each line in the hosts file.  

## ping-sweeper*
Ping Sweeper will ping the subnet entered and report back with hosts which respond to the ping request. Running a ping sweep will report output to screen and also to a file Command Runner will connect to devices listed within devices.txt and perform cli commands requested when running the program. Output will be printed to the screen and also to a file in folder called "output", assuming it is created prior to running the program. Note that some hosts do not respond to ping.
### How to use:
Simply run the application and enter the subnet to sweep. Maintain subnet boundaries by typing the network address for the subnet, for example:  
192.168.1.0/24 - Correct  
192.168.1.1/24 - Incorrect - application will fail  
