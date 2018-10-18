import ipaddress
import subprocess
import socket
import sys

addr = input("Enter a network address format(ex.192.168.1.0/24): ")
ip = ipaddress.ip_network(addr)
all_hosts = list(ip.hosts())
a = 0
all_ip = []
for all_hosts[a] in all_hosts:
    address = all_hosts[a]
    print("=" * 100)
    print("Please wait, ping address: ", address)
    print("=" * 100)
    res = subprocess.call(['ping', '-c', '1', str(address)])
    if res == 0:
        print("ping to", address, "OK")
        print("=" * 100)
        print("Please wait, scanning port...")
        print("=" * 100)
        for port in range(1, 1024 + 1, 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.connect((str(address), port))
                print("Port: ", port)
            except:
                pass
            sock.close()
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
    a += 1
