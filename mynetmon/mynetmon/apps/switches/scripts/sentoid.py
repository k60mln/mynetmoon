# import section
from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime

# var section

#snmp
community_string = 'public'  # From file
ip_address_host = '192.168.1.100'  # From file
port_snmp = 161
OID_sysName = '1.3.6.1.2.1.1.5.0'  # From SNMPv2-MIB hostname/sysname

# function section

def snmp_getcmd(community, ip, port, OID):
    return (getCmd(SnmpEngine(),
                   CommunityData(community),
                   UdpTransportTarget((ip, port)),
                   ContextData(),
                   ObjectType(ObjectIdentity(OID))))

def snmp_get_next(community, ip, port, OID):
    errorIndication, errorStatus, errorIndex, varBinds = next(snmp_getcmd(community, ip, port, OID))
    for name, val in varBinds:

        return (val.prettyPrint())

#code section

sysname = (snmp_get_next(community_string, ip_address_host, port_snmp, OID_sysName))
print('hostname= ' + sysname)