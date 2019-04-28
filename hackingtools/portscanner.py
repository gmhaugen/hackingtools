#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import socket
import subprocess
import sys
import os
import getopt
from datetime import datetime
import struct

"""
This module is a simple portscanner for fast recog in pentesting.
"""
HELPMESSAGE = 'portscanner.py' \
              '' \
              ''

portscan_result = {
    "open": [],
    "closed": []
}

common_ports = [22, 53, 80, 443, 8080]

timeout = 5

def main(argv):
    port = -1
    verbose = False
    dosweep = False
    scan = False
    discover = False
    doping = False
    host = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hsdp:vz:t:", ['-help', 'sweep', 'discover', 'port', 'verbose', 'ping', 'target'])
    except getopt.GetoptError:
        print(HELPMESSAGE)
        sys.exit()

    for opt, arg in opts:
        if opt == "-h":
            print(HELPMESSAGE)
            sys.exit(1)
        elif opt in ("-s", "--sweep"):
            print("scan=true")
            scan = True
        elif opt in ("-d", "--discover"):
            print("discover=true")
            discover = True
        elif opt in ("-p", "--port"):
            print("port=" + arg)
            port = int(arg)
        elif opt in ("-v", "--verbose"):
            print('verbose=true')
            verbose = True
        elif opt in ("-z", "--ping"):
            print("ping=true")
            doping = True
            print(arg)
            if arg == None or arg == "":
                print('Please provide a host for ping')
                sys.exit(1)
            else:
                host = arg
        elif opt in ("-t", "--target"):
            host = arg
        else:
            print('Invalid input')
            print(HELPMESSAGE)

    if discover:
        discover_hosts()

    if dosweep:
        sweep_scan()

    if doping:
        ping_host(host)


    if scan:
        if port == -1:
            print('No ports given, trying common ports')
            for port in common_ports:
                tcp_scan(host, port)
        else:
            tcp_scan(host, port)




def ping_host(ip):
    print('Pinging host ' + ip)
#    response = os.open('ping -n 1 192.168.0.1')
    response = subprocess.call(['ping', '-c', '3', ip])
    if response == 0:
        print('Host is up')
    elif response == 2:
        print('No response from ' + ip)
    else:
        print('Ping to ' + ip + ' failed')


def sweep_scan():
    print('Performing sweep scan')
    response = os.open('ping -n 1 192.168.0.1')


def discover_hosts():
    local_ip = get_local_ip()
    print(local_ip)


def tcp_scan(address, port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1,0))
    connection.settimeout(timeout)

    target = (address, port)

    response = connection.connect_ex(target)

    if response == 0:
        print('Port ' + str(port) + ' is OPEN')
        portscan_result['open'].append(port)
    elif response == 111:
        print('Port ' + str(port) + ' is CLOSED')
        portscan_result['closed'].append(port)

    print(response)


def get_local_ip():
    host_name = socket.gethostname()
    print(host_name)
    host_ip = socket.gethostbyname_ex(host_name)
    return host_ip


if __name__ == "__main__":
	main(sys.argv[1:])
