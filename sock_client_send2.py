# coding:utf-8
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8100
csock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#csock.setblocking(False)
csock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
csock.settimeout(1)
csock.connect((HOST,PORT))
print '发送消息'
while True:
    s=raw_input('>>')
    if not s:
        csock.close()
        break
    csock.send(s)
