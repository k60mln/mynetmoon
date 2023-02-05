import telnetlib

host = '192.168.1.100'
def logging(host):
    telnet = telnetlib.Telnet(host)
    telnet.read_until(b'Username')
    telnet.write(b'admin\n')
    telnet.read_until(b'Password')
    telnet.write(b'zxcvbn\n')
    telnet.read_until(b'>')
    telnet.write(b'reboot\n')
    telnet.read_until(b':')
    telnet.write(b'Y\n')
    telnet.close()

