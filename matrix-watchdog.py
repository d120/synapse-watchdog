#! /usr/bin/env python3

# This script checks every 30 seconds, if the Matrix server is still alive
# If not, the server will be restarted with systemd
# The user, which runs this script, must have sudo rights for systemctl

from http import client
from time import sleep
import datetime
import sys
from subprocess import call

try:
  while True:
    print('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), end='\t', file=sys.stderr)
    try:
      conn = client.HTTPSConnection('matrix.d120.de', 8448, timeout=10)
      conn.connect()
      conn.request("GET", "/_matrix/client/versions")
      ret = conn.getresponse()
      if ret.status != 200:
        raise ValueError("Error")
      print(ret.status, file=sys.stderr)
    except:
      print("error", file=sys.stderr)
      call(["sudo", "systemctl", "restart", "synapse"])
      sleep(90)
    sleep(30)
except KeyboardInterrupt:
  print("")
  print("terminated")
