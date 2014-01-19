# coding:gbk
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8100
csock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#csock.setblocking(False) #有这句则会运行出错，不懂setblocking方法
csock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
csock.settimeout(1)
csock.connect((HOST,PORT))
print '接收消息中……'
while True:
    try:
        data = csock.recv(1024)
    except socket.timeout,e:
        #print type(e)
        continue
    if not data:
        print '关闭与',csock.getpeername(),'的连接'
        csock.close()
        break
    print data

'''
难点：
server关闭了csock仍不会关闭，且recv方法阻塞状态下CTRL+C也无效，怎么才能控制其退出呢？
'''
