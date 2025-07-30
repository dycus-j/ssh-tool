# Python SSH Automation Tool - v1.1

## Objective
A command-line tool built with Python and the Paramiko library to automate SSH connections to remote servers. This tool can execute commands and save the output to a local, timestamped backup file, providing a simple and effective way to remotely gather configuration data.

## Features
* Connects to any specified host using a username and password.
* Takes the target host's IP address as a command-line argument for flexibility.
* Securely prompts for the user's password using `getpass`.
* Executes a given command on the remote server and captures the output.
* Saves the command output to a uniquely named, timestamped file in a local `backups/` directory.
* Includes robust error handling for connection failures and empty user input.

## Technologies Used
* Python
* Paramiko (for SSH connectivity)
* `sys`, `getpass`, `time`, `os` modules
* Ubuntu Server (as the remote target in a virtual lab)

## How to Use
1.  Set up a Python virtual environment and install the required library:
    ```bash
    pip install paramiko
    ```
2.  Create a `backups/` directory in the project folder.
3.  Run the script from the command line, providing the target IP address as an argument.

    ```bash
    python3 ssh-tool.py 192.168.64.5
    ```
4.  You will be prompted to enter the username and password for the remote host.

## Future Improvements
* **v1.2:** Refactor the script to use SSH key-based authentication for a more secure and fully automated workflow, removing the need for password prompts.
