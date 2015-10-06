#!/usr/bin/python

import sys

# This script may eventually be upgraded to filter on signal or quality level
# when deciding what to list.

my_list = []
currentCell = None
for line in sys.stdin:
   line = line.strip()
   if line.startswith('Cell'):
       # Dump the previous one if there was one
       if currentCell: my_list.append(currentCell)
       currentCell = {}
       currentCell['ap_address'] = line.split(":", 1)[1].strip()
   elif not currentCell: continue
   elif line.startswith("Frequency"):
       currentCell["frequency"] = line.split()[0].split(":")[1]
   elif line.startswith("Quality"):
       quality, signal = line.split(" ", 1)
       currentCell["quality"] = quality.split("=")[1]
       currentCell["signal"] = signal.split("=")[1]
   elif line.startswith("ESSID"):
       currentCell["ssid"] = line.split(':')[1].replace('"','')
   elif line.startswith("Encryption"):
       currentCell["encryption"] = line.split(':')[1]

if currentCell: my_list.append(currentCell)

output_sequece = ['ssid', 'encryption', 'ap_address', 'frequency', 'quality', 'signal']
print "\t".join(output_sequece)

# Check for filter otherwise use -100 as infinity
signal_filter = -100
if len(sys.argv) > 1:
   signal_filter = int(sys.argv[1])
   
   # Allow either positive or negative values
   if signal_filter > 0: signal_filter *= -1

for x in my_list:
  if not x['ssid']: continue
  if int(x['signal'].split()[0]) >= signal_filter:
     print "\t".join([x[i] for i in output_sequece])
