#!/usr/bin/env python3
import requests, sys
url = "http://" + sys.argv[1] + ":8080/cgi-bin/sysinfo.json?hosts=1"
sysinforaw = requests.get(url)
if(sysinforaw.status_code < 400):
  sysinfo = sysinforaw.json()
  hosts = sysinfo['hosts']
else:
  print('Bad URL: ',url)
  exit()
for i in hosts:
  url = "http://" + i['ip'] + ":8080/AREDN.png"
  try:
    pngfile = requests.head(url, timeout=5)
    if(pngfile.status_code < 400):
      print ('Found AREDN.png at ', i['name'])
  except:
      print('No AREDN.png at ', i['name'])
exit()
