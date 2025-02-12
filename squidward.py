#!usr/bin/python

'''
This program accepts two text files, one for hosts and one for obtained credentials.
The program then checks the given credentials on every host to see if the host may be logged into via SSH.
Finally, the program checks for anonymous login.
'''

import paramiko 
import random
import socket
import sys

hostList = []
credList = []
openList = []

def connectSSH(host='127.0.0.1',port=22,user=None,passwd=None):
	connectionSuccessful = False
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	socket.setdefaulttimeout(1)
	try:		
		# Check connectivity
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,port))

		# Connect to host
		client.connect(host, port, user, passwd)
		connectionSuccessful = True
	except: pass
	client.close()
	return connectionSuccessful

def asciiArt():
	phraseList = ["Another day, another migraine.\nHEH. HEH. Migraine.","Mayonnaise is not an instrument.","Don't say anything Squidward, remember your karma.","AND IF THERE'S ANYTHING ELSE I CAN DO,\nPlease... HESITATE TO ASK!"]
	randNum = random.randrange(len(phraseList))
	print(  "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⠀⢀⣠⣤⣶⠾⠟⠛⠛⠛⠛⠛⠛⠻⠷⣶⣤⣄⡀⠀⠀⠀⠀⠀\n"
			"⠀⠀⠀⣠⡾⠟⠋⠁⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠈⠙⠻⢷⣄⠀⠀⠀\n"
			"⠀⢀⣾⠋⠀⠀⠀⠀⠶⠶⠿⠛⠛⠛⠛⠛⠛⠿⠶⠶⠀⠀⠀⠀⠙⣷⡀⠀\n"
			"⠀⣿⠃⠀⠀⠀⠀⠀⢀⣠⣤⣤⡀⠀⠀⢀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠘⣿⠀\n"
			"⠘⣿⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣿⠃\n"
			"⠀⠻⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣼⠟⠀\n"
			"⠀⠀⠙⢷⣄⡀⠘⣿⠛⠛⣿⡟⠛⢻⡟⠛⢻⣿⠛⠛⣿⠁⢀⣠⡾⠋⠀⠀\n"
			"⠀⠀⠀⠀⠉⠻⢷⣿⣧⠀⠉⠁⣠⡿⢿⣄⠈⠉⠀⣼⣿⡾⠟⠉⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣶⣾⡟⠀⠀⢻⣷⣶⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⠀⠀⣀⣀⣸⣿⢀⣿⠁⠀⠀⠈⣿⡀⣿⣇⣀⣀⠀⠀⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⣴⡟⠋⢉⣉⣀⣸⡏⠀⠀⠀⠀⢹⣇⣀⣉⡉⠙⢻⣦⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⣿⡀⠘⠛⠛⠉⣹⣷⠀⠀⠀⠀⣾⣏⠉⠛⠛⠃⢀⣿⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⠘⠻⠷⠾⠛⠛⠛⠛⢷⣤⣤⡾⠛⠛⠛⠛⠷⠾⠟⠃⠀⠀⠀⠀\n"
			"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
	print(phraseList[randNum])
	print()
	print("Checking connections...")
	print()

def main():
	# Check for proper number of arguments
	if len(sys.argv) < 3: sys.exit("Usage: python3 squidward.py hosts.txt creds.txt")

	# Print loading screen
	asciiArt()

	# Read hosts file
	file = open(sys.argv[1], "r")
	for host in file: hostList.append(host.strip())
	file.close()

	# Read creds file
	file = open(sys.argv[2], "r")
	line = file.readline()
	while line:
		if line == "": line = file.readline()
		else:
			user = line.strip()
			passwd = file.readline().strip()
			credList.append([user,passwd])
			line = file.readline()
			line = file.readline()
	file.close()

	# Loop through hosts, try given credentials to login
	for host in hostList:
		for creds in credList:
			if connectSSH(host,22,creds[0],creds[1]):
				openList.append("Host:{0}\nUsername:{1}\nPassword:{2}\n".format(host,creds[0],creds[1]))
		
		# Check if anonymous login is allowed
		if connectSSH(host): openList.append("Host:{0} allows anonymous login".format(host))

	# Print out list of successful connects
	if not openList: print("Could not connect to any hosts.\n")
	else:
		for line in openList: print(line)
main()
