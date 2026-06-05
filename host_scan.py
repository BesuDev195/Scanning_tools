import sys
import ipaddress
import platform
import subprocess

def get_network(ip, ip_class):
    ip_class = ip_class.upper()

    if ip_class == "A":
        mask = "255.0.0.0"
    elif ip_class == "B":
        mask = "255.255.0.0"
    elif ip_class == "C":
        mask = "255.255.255.0"
    else:
        raise ValueError("Class must be A, B, or C")

    return ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

def ping_host(ip):
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <IP> <A|B|C>")
        sys.exit(1)

    target_ip = sys.argv[1]
    ip_class = sys.argv[2]

    try:
        network = get_network(target_ip, ip_class)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"\nTarget IP  : {target_ip}")
    print(f"IP Class   : {ip_class.upper()}")
    print(f"Network    : {network}")
    print("\nDiscovering hosts...\n")

    alive_count = 0

    for host in network.hosts():
        if ping_host(host):
            print(f"[+] Host Alive: {host}")
            alive_count += 1

    print(f"\nTotal live hosts found: {alive_count}")

if __name__ == "__main__":
    main()