
import subprocess
import socket

def ping(host,liness):
    result = subprocess.run(['ping', host,'-n', '1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outputs = result.stdout.decode()
    host_name=""
    if outputs.find("unreachable")<0:
        liness=liness+host+" "
        try:
            host_name= socket.gethostbyaddr(host)[0]
            liness=liness+host_name+"\n\r"      
        except socket.error as e:
            liness=liness+host_name+"\n\r"
    return liness
            
n = 0
i=127
ii=1
separetor="-----------------------------------------------------------"
host_to_ping = "192.168.1."
host_to_ping2 = host_to_ping 
liness=""
print("\033c\033[47;34m")
for n in range(ii,i):
    host_to_ping2 = host_to_ping + str(n)
    liness=ping(host_to_ping2,liness)
f = open("out.txt", "w")
f.write(liness)
f.close()