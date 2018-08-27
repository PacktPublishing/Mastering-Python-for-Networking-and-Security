# -*- encoding: utf-8 -*-
import msfrpc
import time

client = msfrpc.Msfrpc({'uri':'/msfrpc', 'port':'5553', 'host':'127.0.0.1', 'ssl': True})
auth = client.login('msf','password')

def processData(consoleId):
    while True:
        readedData = client.call('console.read',[consoleId])
        print(readedData['data'])
        if len(readedData['data']) > 1:
            print(readedData['data'])
        if readedData['busy'] == True:
            time.sleep(1)
            continue
        break
    
if auth:

    console = client.call('console.create')

	#read commands from the file commands_file.txt
	file = open ("commands_file.txt", 'r')
	commands = file.readlines()
	file.close()
	
	# Execute each of the commands that appear in the file
	print(len(commands))
	
	for command in commands:
		resource = client.call('console.write',[console['id'], command])
		processData(console['id'])

    