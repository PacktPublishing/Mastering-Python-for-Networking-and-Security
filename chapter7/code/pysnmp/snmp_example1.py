from pysnmp.hlapi import *

SNMP_HOST = '182.16.190.78'
SNMP_PORT = 161
SNMP_COMMUNITY = 'public'


errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(SNMP_COMMUNITY, mpModel=0),
           UdpTransportTarget((SNMP_HOST, SNMP_PORT)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1][0] or '?'
        )
    )
else:
    for varBind in varBinds:
        print(' = '.join([ x.prettyPrint() for x in varBind ]))