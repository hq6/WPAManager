#!/usr/bin/python

import sys

my_list = []
for line in sys.stdin:
   line = line.strip()
   if line == '--': continue
   my_list.append(line)


foo = set()
for i in xrange(len(my_list) / 2):
   encrypt, ssid = my_list[i*2], my_list[i*2 + 1]
   encrypt, ssid = encrypt.split(':')[1], ssid.split(':')[1].replace('"', '')
   if ssid == '': continue
   foo.add((ssid, encrypt))

print "ssid\tencryption"
for x in foo:
  print "\t".join(x)
   
