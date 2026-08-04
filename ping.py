import platform
import subprocess

def ping_host(host, count=4):
    """
    Pings a target host and displays the output.
    Automatically handles OS-specific flags (-n for Windows, -c for Linux/macOS).
    """
    # Determine the parameter based on OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    command = ["ping", param, str(count), host]

    print(f"\n[*] Pinging {host} with {count} packets...\n")

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        
        print(result.stdout)
        
        if result.returncode == 0:
            print(f"[+] {host} is Up")
        else:
            print(f"[-] {host} appears to be down or unreachable.")
            
    except Exception as e:
        print(f"[-] Error executing ping: {e}")