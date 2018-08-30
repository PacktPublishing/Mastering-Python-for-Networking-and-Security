from pysnmp.entity.rfc3413.oneliner import cmdgen


SNMP_HOST = '182.16.190.78'
SNMP_PORT = 161
SNMP_COMMUNITY = 'public'


snmpCmdGen = cmdgen.CommandGenerator()

snmpTransportData = cmdgen.UdpTransportTarget((SNMP_HOST,SNMP_PORT))


error,errorStatus,errorIndex,binds = snmpCmdGen.getCmd(cmdgen.CommunityData(SNMP_COMMUNITY),snmpTransportData,"1.3.6.1.2.1.1.1.0","1.3.6.1.2.1.1.3.0","1.3.6.1.2.1.2.1.0")
if error:
	print("Error"+error)
else:
	if errorStatus:
		print('%s at %s' %(errorStatus.prettyPrint(),errorIndex and binds[int(errorIndex)-1] or '?'))
	else:
		for name,val in binds:
			print('%s = %s' % (name.prettyPrint(),val.prettyPrint()))
