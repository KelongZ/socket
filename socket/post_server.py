# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:54:58 2019

@author: Kelong
"""

import socket
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 8000))
sk.listen(2)

print('waiting for connecting')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    conn, addr = sk.accept()
    print('connected by', addr)
    while 1:
        data = conn.recv(1024)
        cmd,filename,filesize = data.decode('utf8').split('|')
        path = os.path.join(BASE_DIR,'yuan',filename)
        filesize = int(filesize)

        has_receive = 0
        with open(path,'ab') as f:
            while has_receive != filesize:
                data = conn.recv(1024)
                f.write(data)
                has_receive += len(data)

sk.close()