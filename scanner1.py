# Nmap scanner without nmap module
import socket
import sys

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <IP_ADDRESS>")
    sys.exit(1)

target = sys.argv[1]

print(f"Scanning {target}...")

for port in range(1, 1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    if sock.connect_ex((target, port)) == 0:
        print(f"Port {port} is OPEN")

    sock.close()