import ipaddress
import os
import requests
import socket
import sys
from ip2geotools.databases.noncommercial import DbIpCity


def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f'"{res.ip_address}","{res.country}","{res.region}","{res.city}"')

if __name__ == "__main__":
    # Check for command line arg
    if len(sys.argv) !=2:
        print("Error- this program requires the following usage:\n")
        print("    python ip2country.py IP_ADDRESS_LIST_FILENAME.txt")
        exit(-1)
    
    filename=sys.argv[1]

    if os.path.exists(filename):
        # Get list of IPs from text file
        ip_list = []

        with open(filename, encoding="UTF-8") as ip_file:
            for line in ip_file:
                # Check line looks like an IP
                try:
                    line = line.lstrip().rstrip()
                    new_ip = ipaddress.ip_address(line)
                    ip_list.append(line)
                    print(f"added {line}")

                except ValueError as v:
                    print(v)
                    exit(-3)

        print(f"{len(ip_list)} ip addresses added for lookup.")

        for ip in ip_list:
            printDetails(ip)
    else:
        print(f"IP address list file: {filename} does not exist. Exiting.")
        exit(-2)