import ftplib
import shodan
import socket

ips =[]

shodanKeyString = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'
shodanApi = shodan.Shodan(shodanKeyString)
results = shodanApi.search("port: 21 Anonymous user logged in")

for match in results['matches']:
    if match['ip_str'] is not None:
        ips.append(match['ip_str'])
    

  
print("Sites found: %s" %len(ips))

for ip in ips:
	try:
		print(ip)
		#server_name = socket.gethostbyaddr(str(ip))
		server_name = socket.getfqdn(str(ip))
		print("Connecting to ip: " +ip+ " / Server name:" + server_name[0])
		ftp = ftplib.FTP(ip)
		ftp.login()
		print("Connection to server_name %s" %server_name[0])
		print(ftp.retrlines('LIST'))
		ftp.quit()
		print("Existing to server_name %s" %server_name[0])
	except Exception as e:
		print(str(e))
		print("Error in listing %s" %server_name[0])