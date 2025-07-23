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


def create_connection(host, username, password):
    # Establishes the ssh connection via paramiko SSHClient object
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"\n[+] Connecting to {hostname}...")
        client.connect(hostname=host, username=username, password=password)
        print("✓ Connection successful!")
        return client
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return None
    
    
def exec_command(ssh_client, command):
    if not ssh_client:
        return None
    
    print(f"[+] Executing command: '{command}'...")
    stdin, stdout, stderr = ssh_client.exec_command(command)
    
    error = stderr.read().decode()
    if error:
        print(f"Error executing command: {error}")
        return None
    
    return stdout.read().decode()

        
        
def main():
    # Get hostname from CLI
    host = get_hostname()
    
    # Get host credentials 
    username, password = get_credentials(host)
    
    # Establish SSH connection
    client = create_connection(host, username, password)
    
    # Define command and run
    cli_command = "ip a"
    command_output = exec_command(client ,cli_command)
    