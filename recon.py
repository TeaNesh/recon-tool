import os
import platform
import socket
from datetime import datetime

report_file = "recon_report.txt"

def write_to_report(text):
    with open(report_file, "a") as f:
        f.write(text + "\n")

print("Generating Recon Report...\n")

write_to_report("=== SYSTEM RECON REPORT ===")
write_to_report(f"Generated on: {datetime.now()}\n")

# OS Information
os_info = f"Operating System: {platform.system()} {platform.release()}"
print(os_info)
write_to_report(os_info)

# Hostname and IP
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

host_info = f"Hostname: {hostname}\nIP Address: {ip_address}"
print(host_info)
write_to_report(host_info)

# Running Processes
write_to_report("\n=== Running Processes ===")
os.system("tasklist >> recon_report.txt")

# Open Ports
write_to_report("\n=== Open Ports ===")
os.system("netstat -ano >> recon_report.txt")

print("\nRecon report saved to recon_report.txt")
