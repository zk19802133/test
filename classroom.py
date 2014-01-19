# coding:gbk
import urllib
import urllib2
from lxml import html
import re

classes=[]
CLASSNAME = '文泰'
c1=[str(k) for k in range(1,6)]
c2=['0'+str(k) for k in range(1,10)]+[str(k) for k in range(10,22)]
for i in c1:
    for j in c2:
        CLASSID=i+j
        url = 'http://202.114.224.81:7777/pls/wwwbks/xxcx.jskbcx1'
        data={'classname':CLASSNAME,'classid':CLASSID}
        d=urllib.urlencode(data)
        req=urllib2.Request(url,d)
        res=urllib2.urlopen(req)
        result=res.read()
        res.close()
        root=html.fromstring(result)
        try:
            notice=root.xpath('//td[@valign="top"]/child::text()')[2].encode('gbk')
        except IndexError:
            continue
        print notice
        if re.findall('有0次',notice):
            classes.append(CLASSNAME+CLASSID)
print '空教室：'
for c in classes:
    print c
    
