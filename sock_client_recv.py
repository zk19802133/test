# coding:gbk
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8100
csock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#csock.setblocking(False) #�����������г�������setblocking����
csock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
csock.settimeout(1)
csock.connect((HOST,PORT))
print '������Ϣ�С���'
while True:
    try:
        data = csock.recv(1024)
    except socket.timeout,e:
        #print type(e)
        continue
    if not data:
        print '�ر���',csock.getpeername(),'������'
        csock.close()
        break
    print data

'''
�ѵ㣺
server�ر���csock�Բ���رգ���recv��������״̬��CTRL+CҲ��Ч����ô���ܿ������˳��أ�
'''
