# Ping sweep script

import subprocess
import os

for x in range(256):
  number = str(x)
  ping = os.system("timeout 1 ping -c 1 10.10.10." + number + " >/dev/null")
  if ping == 0:
    print "10.10.10." + number + "[ON]"
  else:
    print "10.10.10." + number + "[OFF]"
