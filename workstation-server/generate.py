#!/usr/bin/env python3

"""
This script generates a list of packages that should be removed
from RedHat 7 workstation to keep it identical to server.
"""

# Packages name to be ignored.
IGNORE_LIST_SUBSTRING = ['redhat']

# To generate the list of packages, run in each version: rpm -qa --qf "%{NAME}\n"
with open('redhat8-workstation-packages.txt', 'r') as f:
    workstation_packages = [line.strip().rstrip() for line in f.readlines()]

with open('redhat8-server-packages.txt', 'r') as f:
    server_packages = [line.strip().rstrip() for line in f.readlines()]

# Remove ignored items.
for line in workstation_packages:
    for word in IGNORE_LIST_SUBSTRING:
        if word in line:
            workstation_packages.remove(line)

for line in server_packages:
    for word in IGNORE_LIST_SUBSTRING:
        if word in line:
            server_packages.remove(line)


# Convert the list to sets (to allow difference between sets).
wps = set(workstation_packages)
sps = set(server_packages)

# Generate the different of the sets (packages present in workstation but not in server).
remove_list = sorted(wps - sps)

# Print the list and command to be run.
print('-'*40)
print('Run the following command in your workstation version: ')
print('-'*40)
print('yum -y remove {}'.format(' '.join(remove_list)))
print('-'*40)
