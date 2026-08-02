import os
import nmap

def run_nmap(target, ports="1-1024", args="-sV"):
    # Windows-specific PATH fallback for Nmap
    nmap_paths = [
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        r"C:\Program Files\Nmap\nmap.exe"
    ]
    
    selected_path = None
    for path in nmap_paths:
        if os.path.exists(path):
            selected_path = path
            break

    try:
        if selected_path:
            nm = nmap.PortScanner(nmap_search_path=(selected_path,))
        else:
            nm = nmap.PortScanner()

        print(f"\n[+] Scanning: {target}")
        print(f"[+] Target Ports: {ports} | Arguments: {args}\n")
        
        nm.scan(hosts=target, ports=ports, arguments=args)

        for host in nm.all_hosts():
            print(f"[+] Host: {host} ({nm[host].hostname()})")
            print(f"[+] State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                print(f"\n--- Protocol: {proto.upper()} ---")
                ports_list = nm[host][proto].keys()
                for port in sorted(ports_list):
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port].get('name', 'unknown')
                    version = nm[host][proto][port].get('version', '')
                    product = nm[host][proto][port].get('product', '')
                    
                    print(f"  Port: {port:<6} State: {state:<8} Service: {service} {product} {version}".strip())
                    
    except Exception as e:
        print(f"[-] Nmap Execution Error: {e}")