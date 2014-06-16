#!/usr/bin/env python



import os
import time

while (1):

	p = os.popen('airport en0 sniff 11',"r")

	time.sleep (30)

	r = os.popen('scp airport*.cap username@host:/home/path/',"r")

	s = os.popen('killall | grep airport',"x")

	d = os.popen('/usr/sbin/networksetup -setairportnetwork en0 BlueNet',"x")

	m = os.popen('scp /tmp/airport*.cap username@host:/home/path/',"r")

	e = os.popen('rm /tmp/airport*.cap',"r")

	time.sleep (30)
