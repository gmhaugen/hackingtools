#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import socket
import subprocess
import sys
import os
import getopt
from datetime import datetime

"""
This module is a simple portscanner for fast recog in pentesting.
"""
HELPMESSAGE = 'helpmessage'

def main(argv):
    port = 0
    verbose = False
    dosweep = False
    host = ''

    try:
        opts, args = getopt.getopt(argv, "hsp:")
    except getopt.GetoptError:
        print(HELPMESSAGE)
        sys.exit()

    for opt, arg in opts:
        if opt == "-h":
            print(HELPMESSAGE)
        elif opt in ("-s", "--sweep"):
            dosweep = True
        elif opt == "-p":
            port = arg
        else:
            print('Invalid input')
            print(HELPMESSAGE)

        if opt in ("-d", "--verbose"):
            verbose = True

        if opt in ("-z", "--ping"):
            host = arg
            ping_host(host)

    if dosweep:
        sweep_scan()


def ping_host(ip):
    print('Pinging host %s', ip)


def sweep_scan():
    print('Performing sweep scan')
    response = os.open('ping -n 1 192.168.0.1')



if __name__ == "__main__":
	main(sys.argv[1:])
