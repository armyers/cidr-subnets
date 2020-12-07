#!/usr/bin/env python3
#

import os
import sys
from ipaddress import ip_network

def main(argv):
    """
    """
    if not (len(argv) >= 2 and len(argv) <= 3):
        print('Usage: %s cidr-block [additional-subnet-split]' % argv[0])
        sys.exit(1)

    network = argv[1]
    ip, netmask = network.split('/')
    octets = ip.split('.')
    while len(octets) < 4:
        # add 0's to fill it out
        octets += ['0']
    # put the ip back together
    ip = '.'.join(octets)
    # put the network back together
    network = ip + '/' + netmask

    net = ip_network(network, strict=False)
    subnet_split = 0
    if len(argv) == 3:
        subnet_split = int(argv[2])
    subnets = list(net.subnets(subnet_split))

    for subnet in subnets:
        print ("net %s : broadcast %s : hosts %s" % (subnet.exploded, subnet.broadcast_address, subnet.num_addresses))
    print("%s subnets" % int(len(subnets)))

if __name__ == '__main__':
    main (sys.argv)
