from netmiko import ConnectHandler
from datetime import datetime
import re

switch = {
     'device_type': 'cisco_ios',
     'ip':   '10.134.217.33',
     'username': 'prime',
     'password': 'Dnekrf55',
     'verbose': False,
}

start_time = datetime.now()

net_connect = ConnectHandler(**switch)
output = net_connect.send_command("show version")

line = re.findall(r'Power supply serial number', output)[0:2]

print(line)

end_time = datetime.now()
total_time = end_time - start_time
print(total_time)