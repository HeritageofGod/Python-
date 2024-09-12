

# OYEKOLA ELIZABETH FUNMILAYO
# HND/230555
"""

#Variabale Declaration
x= 10
print("The initial value of x is ",x)
#Redeclaration of variable
x = 20
print("The new value for x is ",x)

import os
import socket

def check_connectivity():
    # Check if the system can connect to the internet (Google DNS as an example)
    response = os.system("ping -c 4 8.8.8.8")  # Ping Google's public DNS server
    if response == 0:
        print("Internet connection: Available")
    else:
        print("Internet connection: Unavailable")

def get_ip_address():
    # Get the IP address of the system
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Your computer's IP address is: {ip_address}")

def check_website_reachability(url):
    try:
        # Try to resolve the website's hostname to an IP address
        ip = socket.gethostbyname(url)
        print(f"Website {url} is reachable (IP: {ip})")
    except socket.error:
        print(f"Website {url} is not reachable")

if __name__ == "__main__":
    print("Network Troubleshooting:")

    # Check if the computer has internet connectivity
    check_connectivity()

    # Get the IP address of the local machine
    get_ip_address()

    # Check if a specific website is reachable
    website = "www.google.com"
    check_website_reachability(website)
