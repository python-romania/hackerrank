import os
from time import sleep
hostname = "google.com"

def ping(address):
    while not os.system('ping %s -n 1 > NUL' % (address,)):
        sleep(1)
        print(address, 'is online')

ping(hostname)
