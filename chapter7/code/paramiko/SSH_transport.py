import paramiko

def ssh_command(ip, user, passwd, command):
    transport = paramiko.Transport(ip)
    try:
        transport.start_client()
    except Exception as e:
        print(e)
    
    try:
        transport.auth_password(username=user,password=passwd)
    except Exception as e:
        print(e)
        
    if transport.is_authenticated():
        print(transport.getpeername())
        channel = transport.opem_session()
        channel.exec_command(command)
        response = channel.recv(1024)
        print('Command %r(%r)-->%s' % (command,user,response))

if __name__ == '__main__':
	username = input("Enter username: ")
	password = getpass.getpass(prompt="Enter password: ")
	command= 'ifconfig'
	run_ssh_command('localhost',username, password, command)

#ssh_command('192.168.56.101', 'msfadmin', 'msfadmin','ls -la')