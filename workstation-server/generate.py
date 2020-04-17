#!/usr/bin/env python3

"""
This script generates a list of packages that should be removed
from RedHat 7 workstation to keep it identical to server.
"""

from itertools import filterfalse

# Packages name to be ignored, otherwise they will remove subscription-manager.
IGNORE_LIST_SUBSTRING = [
    'redhat', 
    'subscription', 
    'initial-setup', 
    'python-syspurpose', 
    'rhsm-gtk'
]

# To generate the list of packages, run in each version: rpm -qa --qf "%{NAME}\n"
with open('redhat7-workstation-packages.txt', 'r') as f:
    workstation_packages = [line.strip().rstrip() for line in f.readlines()]

with open('redhat7-server-packages.txt', 'r') as f:
    server_packages = [line.strip().rstrip() for line in f.readlines()]


def determine(line):
    for word in IGNORE_LIST_SUBSTRING:
         if word in line:
             return True
    return False

workstation_packages[:] = filterfalse(determine, workstation_packages)
server_packages[:] = filterfalse(determine, server_packages)

# Convert the list to sets (to allow diWfference between sets).
wps = set(workstation_packages)
sps = set(server_packages)

# Generate the different of the sets (packages present in workstation but not in server).
remove_list = sorted(wps - sps)

# Print the list and command to be run.
print('-'*40)
print('Run the following command in your workstation version: ')
print('-'*40)
print('yum remove {}'.format(' '.join(remove_list)))
print('-'*40)
