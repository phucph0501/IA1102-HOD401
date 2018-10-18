import subprocess
import socket
import sys

address = input("Input Address: ")
addressIP = socket.gethostbyname(address)
print("=" * 100)
print("Please wait, ping address {}...".format(addressIP))
print("=" * 100)
res = subprocess.call(['ping', '-c', '1', address])
if res == 0:
    print("ping to", address, "OK")
    print("=" * 100)
    print("Please wait, scanning remote host...")
    print("=" * 100)
    start_range = int(input("Enter the start of Port range: "))
    end_range = int(input("Enter the end of Port range: "))
    for port in range(start_range, end_range + 1, 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((addressIP, port))
            print("Port: ", port)
        except:
            pass
        sock.close()
elif res == 2:
    print("no response from", address)
    sys.exit()
else:
    print("ping to", address, "failed!")
    sys.exit()
