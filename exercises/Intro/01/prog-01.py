import os       # For getpid()
import socket   # For gethostname()

def main():
    # Get the system's hostname (equivalent to gethostname() in C)
    hostname = socket.gethostname()

    # Get the current process ID (equivalent to getpid() in C)
    pid = os.getpid()

    # Print the hostname and process ID
    print(f"Hostname: {hostname}, pid: {pid}")

if __name__ == "__main__":
    main()
