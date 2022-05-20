Originally forked from another source but I have used for so long I cannot recall.

CLI Runner will connect to devices listed within devices.txt and perform cli commands requested when running the program. Output will be printed to the screen and also to a folder called "Output" assuming it is created prior to running the program.

Requirements:

python3
python3-netmiko
python3-pyfiglet

How to use:

Edit the hosts file with the list of devices which are to have the single command entered and save in the format required by the application. E.G. SW1, 192.168.1.1
Once the hosts file is complete, simply run the application, it will ask for the command to be entered and then attempt to perform this on each line in the hosts file.
