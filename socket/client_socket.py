# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:04:48 2019

@author: Kelong
"""

import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1',8000))

while 1:
    inp = input(">>>")
    if inp=='exit':
        break
    sk.send(inp.encode('utf8'))
    
    # 解决过长字节一次性输出
    result_len = int(sk.recv(1024).decode('utf8'))
    sk.send('ok'.encode('utf8')) # 解决粘包现象
    print(result_len)
    data = bytes()
    while len(data)!=result_len:
        recv = sk.recv(1024)
        data+=recv
        
    #data = sk.recv(1024)
    print(data.decode('gbk'))
    

sk.close()