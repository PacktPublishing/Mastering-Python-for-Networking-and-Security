#!/usr/bin/python
# -*- coding: utf-8 -*-
import pxssh
import getpass

try:                                                            
    connection = pxssh.pxssh()
    hostname = input('hostname: ')
    username = input('username: ')
    password = getpass.getpass('password: ')
    connection.login (hostname, username, password)
    connection.sendline ('ls -l')
    connection.prompt()
    print(connection.before)
    connection.sendline ('df')
    connection.prompt()
    print(connection.before)
    connection.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(str(e))
