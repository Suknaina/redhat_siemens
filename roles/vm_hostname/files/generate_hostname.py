#!/usr/bin/env python3
import random
import string
import sys
import os

def generate_hostname(location, os_family):
    if location.lower() == "bengaluru":
        prefix = "inblrpr"
    elif location.lower() == "pune":
        prefix = "inpunaa"
    else:
        raise ValueError("Unsupported location")

    if os_family.lower() == "windows server":
        suffix = "wspr"
    elif os_family.lower() == "windows client":
        suffix = "wcpr"
    elif os_family.lower() == "linux":
        suffix = "lnpr"
    else:
        raise ValueError("Unsupported OS family")

    hostnames_file_path = '/var/lib/awx/projects/sukanya/siemens/redhat_siemens/meta_files/hostnames.txt'

    while True:
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        hostname = f"{prefix}{random_part}{suffix}"

        if os.path.exists(hostnames_file_path):
            with open(hostnames_file_path, 'r') as f:
                existing_hostnames = f.read().splitlines()
            if hostname not in existing_hostnames:
                break
        else:
            break

    with open(hostnames_file_path, 'a') as f:
        f.write(hostname + '\n')

    return hostname

if __name__ == "__main__":
    location = sys.argv[1]
    os_family = sys.argv[2]
    print(generate_hostname(location, os_family))

