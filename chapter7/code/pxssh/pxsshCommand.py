#!/usr/bin/python
# -*- coding: utf-8 -*-
import pxssh

hostname = 'localhost'
user = 'user'
password = 'password'
command = 'df -h'


def send_command(ssh_session, command):
	ssh_session.sendline(command)
	ssh_session.prompt()
	print(ssh_session.before)


def connect(hostname, username, password):
	try:
		s = pxssh.pxssh()
		if not s.login(hostname, username, password):
			print("SSH session failed on login.")
		return s
	except pxssh.ExceptionPxssh as e:
		print('[-] Error Connecting')
		print(str(e))
	 

def main():
    session = connect(host, user, password)
    send_command(session, command)
    session.logout()

if __name__ == '__main__':
    main()


