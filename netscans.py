
import subprocess
import socket

def ping(host,liness):
    result = subprocess.run(['ping', host,'-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outputs = result.stdout.decode()
    host_name=""
    if outputs.find("unreachable")<0:
        liness=liness+"<tr><th>"+host+"</th>"
        try:
            host_name= socket.gethostbyaddr(host)[0]
            liness=liness+"<th>"+host_name+"</th><tr>\n"      
        except socket.error as e:
            liness=liness+"<th>"+" "+"</th></tr>\n" 
    return liness
            
n = 0
i=127
ii=1
separetor="-----------------------------------------------------------"
host_to_ping = "192.168.1."
host_to_ping2 = host_to_ping 
print("\033c\033[47;34m")
liness="<html><head><title>network scan report</title><style>\ntable,th,td{\nborder :1px solid black\n}\n</style></head><body><table>"
for n in range(ii,i):
    host_to_ping2 = host_to_ping + str(n)
    liness=ping(host_to_ping2,liness)
liness=liness+"</table></body></html>"
f = open("out", "w")
f.write(liness)
f.close()