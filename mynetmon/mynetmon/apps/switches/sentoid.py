# import section
from pysnmp.hlapi import *
from ipaddress import *
from datetime import datetime

# var section

#snmp
community_string = 'derfnutfo'  # From file
#ip_address_host = '192.168.1.100'  # From file
ip_address_host = '192.168.1.100'  # From file
port_snmp = 161
OID_snmp = '1.3.6.1.2.1.47.1.1.1.1.11.1'

#аптайм надо распарсить 1.3.6.1.2.1.1.3.0
#файл прошивки 1.3.6.1.4.1.25506.2.3.1.4.2.1.2.524290
#серийник 1.3.6.1.2.1.47.1.1.1.1.11.1
#software version reliz 1.3.6.1.2.1.47.1.1.1.1.10.1
#маска .1.3.6.1.4.1.25506.8.35.18.1.2.0
#айпи адрес 1.3.6.1.4.1.25506.8.35.18.1.1.0
#полная модель коммутатора 1.3.6.1.2.1.47.1.1.1.1.13.1.
#просмотр vlan 1.3.6.1.2.1.2.2.1.2.12
#просмотр локации 1.3.6.1.2.1.1.6.0
#просмотр контактов 1.3.6.1.2.1.1.4.0
#прсомотр локального времени 1.3.6.1.4.1.25506.2.3.1.1.3.0
#просмотр количества исходящих пакетов с ошибками на порту, ласт цифра номер порта '1.3.6.1.2.1.2.2.1.20.1'
# Пример просмотра счетчика входящих unicast пакетов на интерфейсе, ласт цифра номер интерфейса '1.3.6.1.2.1.2.2.1.10.1'
# Пример просмотра счетчика исходящих unicast пакетов на интерфейсе, ласт цифра номер интерфейса '1.3.6.1.2.1.2.2.1.16.1'
# статус порта 1-ап 2-даун последняя цифра номер порта '1.3.6.1.2.1.2.2.1.8.3'
# #name port'1.3.6.1.2.1.47.1.1.1.1.7.21'
# #name switch'1.3.6.1.2.1.1.5.0'
# From SNMPv2-MIB hostname/sysname

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

#sysname = (snmp_get_next(community_string, ip_address_host, port_snmp, OID_sysName))
#print('hostname= ' + sysname)


def sysname(ip):
    #sysname = ip + 'В ответе'
    try:
        name = (snmp_get_next(community_string, ip, port_snmp, OID_snmp)) # ip
        return name
    except:
        pass

def sysdetail(ip, oidd):
    #sysname = ip + 'В ответе'
    try:
        sysdet = (snmp_get_next(community_string, ip, port_snmp, oidd))
        return sysdet
    except:
        pass