import time
import nmap
from scan import run_nmap


time.sleep(0.5)
print("██████╗ ██╗      █████╗  ██████╗██╗  ██╗██████╗ ██╗   ██╗\n"
      "██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██╔══██╗╚██╗ ██╔╝\n"
      "██████╔╝██║     ███████║██║     █████╔╝ ██████╔╝ ╚████╔╝ \n"
      "██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██╔═══╝   ╚██╔╝  \n"
      "██████╔╝███████╗██║  ██║╚██████╗██║  ██╗██║        ██║   \n"
      "╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝   \n"
      "                                                         ")

time.sleep(0.5)
print("[*] Starting The BlackPy Framework...")
time.sleep(5)
print("[*] Loading Modules...")
time.sleep(1.5)
print("[+] Success!")
print("""Available Commands:
=========================================================================
[>] Scan: Scans Specified Target IP Address And Ports
[>] Help: Displays The Help Menu
[>] Exit: Exits BlackPy""")


while True: 
    user_input = input("BlackPy> ").strip()
    args=user_input.split()
    if not args:
        continue
    command = args[0].lower()

    if command == "exit":
        print("[*] Exiting BlackPy...")
        time.sleep(1)
        break

    elif command == "help":
        print("===Available Commands===")
        print("[>] scan: {Target-IP} {Ports}: Scans The Specified Target IP Address And Ports")
        print("[>] help: Displays This Help Menu")
        print("[>] exit: Exits BlackPy")
    elif command == "scan":
        if len(args) < 2:
             print("[+] Usage: scan {Target-IP} [Optional{Port(s)}")
             print("[+] Example: scan 192.168.1.1 80,443")
        else:
            target_ip = args[1]
            ports_to_scan = args[2] if len(args) > 2 else "1-1024"
            run_nmap(target_ip, ports=ports_to_scan)
    else:
        print(f"[-] Unknown Command: {command}. Type 'help' for a list of available commands.")


