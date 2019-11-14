# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:04:48 2019

@author: Kelong
"""

import socket
import os

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8000))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    inp=input('>>>').strip() # post|11.png

    cmd,path = inp.split('|')

    path = os.path.join(BASE_DIR,path)

    filename = os.path.basename(path)
    # get file size
    file_size = os.stat(path).st_size

    file_info = 'post|%s|%s'%(filename,file_size)
    sk.sendall(file_info.encode('utf8'))

    has_sent = 0
    with open(path,'rb') as f:
        while has_sent!=file_size:
            data = f.read(1024)
            sk.sendall(data)
            has_sent += len(data)

    print('上传成功')

sk.close()