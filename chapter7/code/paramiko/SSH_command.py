#!/usr/bin/env python3
import getpass
import paramiko

HOSTNAME = 'localhost'
PORT = 22

def run_ssh_command(username, password, command, hostname=HOSTNAME, port=PORT):
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.load_system_host_keys()
	ssh_client.connect(hostname, port, username, password)
	ssh_session = client.get_transport().open_session()
		if ssh_session.active:
			stdin, stdout, stderr = ssh_client.exec_command(command)
			print(stdout.read())
	return

if __name__ == '__main__':
	username = input("Enter username: ")
	password = getpass.getpass(prompt="Enter password: ")
	command= 'ifconfig'
	run_ssh_command(username, password, command)
