import os
import sys
import re


if len(sys.argv) != 2:
        print "\nUsage: python " + sys.argv[0] + " <domain>\n"
        print "Example: python " + sys.argv[0] + "domain.com\n"
        sys.exit(0)
else:
        host = sys.argv[1]

dns_servers = os.popen("host -t ns " + host + "| cut -d \" \" -f4").readlines()

for i in dns_servers:
        scan = os.popen("host -l " + host + " " + i).read()
        check = re.findall('Transfer failed', scan)
        if "Transfer failed" not in check:
                print "[+] " + scan
        else:
                print "[*] Failed: " + i
