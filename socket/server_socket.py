# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:54:58 2019

@author: Kelong
"""

import socket
import subprocess

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',8000))
sk.listen(2)

print('waiting for connecting')

while 1:
    conn,addr = sk.accept()
    print('connected by', addr)
    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data: break
        
        #获取cmd指令结果
        obj = subprocess.Popen(data.decode('utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        
        # 发送cmd结果长度
        result_len = str(len(cmd_result)).encode('utf8')
        conn.sendall(result_len)
        
        conn.recv(1024) # 解决粘包现象
        
        conn.sendall(cmd_result)

sk.close()