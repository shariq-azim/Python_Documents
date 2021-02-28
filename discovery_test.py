import socket

def connect(hostname, port):
    print(hostname, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0
  

print("start")
'''for i in range(1,10):
    res = connect("192.168.0."+str(i), 80)
    if res:
        print("Device found at: ", "192.168.0."+str(i) + ":"+str(80))'''

#import nmap

#nm = nmap.PortScanner()
'''nm.scan(hosts='192.168.1.0/29', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

for host, status in hosts_list:
    print('{0}:{1}'.host)
 '''


import os
os.system('net view > conn.tmp')
f = open('conn.tmp', 'r')
f.readline();f.readline();f.readline()

conn = []
host = f.readline()
while host[0] == '\\':
    conn.append(host[2:host.find(' ')])
    host = f.readline()

print (conn)
f.close() 
