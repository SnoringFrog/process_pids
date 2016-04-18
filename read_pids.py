#! /usr/bin/python3

import os.path

pids_file = "pids.txt"
current_pid_file = "current_pid.txt"

def process_pids():
	for pid in pids:
		with open(current_pid_file,'w') as f:
			f.write(pid+"\n")
		print("Processing pid: "+pid)

## main 
try:
	with open(pids_file) as f:
		pids = f.read().splitlines()
except IOError:
	print("File "+pids_file+" not found")
	exit(1)

pids.sort(key=int)

if os.path.isfile(current_pid_file):
	with open(current_pid_file,'r') as f:
		current_pid = f.read().strip()

	#find current_pid in list, truncate till then
	if current_pid.strip() != "":
		del pids[:pids.index(current_pid)]
	
process_pids()
