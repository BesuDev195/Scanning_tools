# scanner with module
import nmap
import sys

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <IP>")
    sys.exit(1)

target = sys.argv[1]

scanner = nmap.PortScanner()

scanner.scan(target, '1-1024')

for host in scanner.all_hosts():
    print(f"Host: {host}")

    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")

        ports = scanner[host][proto].keys()

        for port in sorted(ports):
            state = scanner[host][proto][port]['state']
            print(f"Port {port}: {state}")