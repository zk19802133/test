# coding:gbk
import select
import socket
#import Queue
'''
����
ʵ�ֶ���ͻ���֮���շ���Ϣ���ͻ��˿�������Ƶ���룬��ͬƵ�����Կ���������˵����
����ʵ�ֿͻ��˿�������˵������һ����ʵ��Ƶ������
'''
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8100
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.setblocking(0)#?
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.settimeout(3)
server.bind((HOST,PORT))
server.listen(10)
inp = [server]
outp = []
err = []
#message={}
timeout = 3 #��ʱ����
count = 0
print '������������'
while inp:
    #print 'select waiting...'
    rs,ws,es = select.select(inp,outp,err,timeout)
    if not (rs or ws or es):
        pass
    else:
        #print 'rs ->',len(rs),' ws ->',len(ws),' es ->',len(es)
        for s in rs:
            if s is server:
                cs,addr = s.accept()
                print 'connected from',addr
                inp.append(cs)
                count = count+1
                print '����������',count
            else:
                print 'Event from',s.getpeername()
                data = s.recv(1024)
                if not data:
                    print '�Ͽ�����',s.getpeername(),'������'
                    count = count-1
                    inp.remove(s)
                    s.close()
                    if len(inp)==1 and inp[0] is server:
                        inp.remove(server)
                        print '����ȫ������'
                    break
                data = str(s.getpeername())+': '+data
                #print data
                for c in inp:
                    if (c is not server) and (c is not s):
                        c.send(data)
                        print '����',s.getpeername(),'����Ϣ�ѷ�����',c.getpeername()
                    
print '�ر�server'
server.close()
