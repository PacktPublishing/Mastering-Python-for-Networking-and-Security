# -*- encoding: utf-8 -*-
import pynexpose

#params connection
serveraddr = 'serveraddr'
port = 3780
username = 'username'
password = 'password'

n = pynexpose.NeXposeServer(serveraddr, port, username, password)
response = n.asset_group_listing()
print response+"\n"
response = n.engine_listing()
print response+"\n"
response = n.report_listing()
print response+"\n"
n.logout()
