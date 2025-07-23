import paramiko
import getpass
import sys
import time

def get_hostname():
    # Gathers and validates hostname from command-line arguements.
    
    if len(sys.argv) < 2:
        print("Error: Please provide an IP address as an argument")
        print("Example: python3 ssh_tool.py 192.168.64.1")
        sys.exit(1)
        
        return sys.argv[1]
        
    

def get_credentials(host):
    # Gathers connection credentials

    username = input(f"Enter username for {host} [default: your_username]: ")
    if not username:
        print("Error: Username cannot be empty.")
        sys.exit(1)
    
    password = getpass.getpass(f"Enter password for {username}@{host}")
    return username, password
        
        
def main():
    host = get_hostname()
    
    username, password = get_credentials(host)