# coding:utf-8
import select
import socket
#import Queue
'''
需求：
实现多个客户端之间收发消息，客户端可以输入频道码，相同频道可以看到其他人说话。
首先实现客户端看到别人说话，下一步再实现频道区分
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
timeout = 3 #超时秒数
count = 0
print '服务器已启动'
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
                print '在线人数：',count
            else:
                print 'Event from',s.getpeername()
                data = s.recv(1024)
                if not data:
                    print '断开来自',s.getpeername(),'的连接'
                    count = count-1
                    inp.remove(s)
                    s.close()
                    if len(inp)==1 and inp[0] is server:
                        inp.remove(server)
                        print '连接全部结束'
                    break
                data = str(s.getpeername())+': '+data
                #print data
                for c in inp:
                    if (c is not server) and (c is not s):
                        c.send(data)
                        print '来自',s.getpeername(),'的消息已发送至',c.getpeername()
                    
print '关闭server'
server.close()
