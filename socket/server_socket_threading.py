# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:54:58 2019

@author: Kelong
"""

import socketserver
import subprocess

class MyServer(socketserver.BaseRequestHandler):
    # 重写父类Handle函数
    def handle(self):
        conn = self.request
        addr = self.client_address
        while True:
            try:
                # 收消息
                data = conn.recv(1024)
                print("收到{0}客户端的消息是{1}".format(addr,data.decode("utf-8")))
            except Exception as e:
                print(e)
                break
            if not data: break
            # 获取cmd指令结果
            obj = subprocess.Popen(data.decode('utf8'), shell=True, stdout=subprocess.PIPE)
            cmd_result = obj.stdout.read()
            # 发送cmd结果长度
            result_len = str(len(cmd_result)).encode('utf8')
            conn.sendall(result_len)

            conn.recv(1024)  # 解决粘包现象

            conn.sendall(cmd_result)
        conn.close()


if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)
    s.serve_forever()