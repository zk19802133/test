# -*- coding: utf-8 -*-

import MySQLdb
import re
import getpass
import time

dataf = (
         # '2000W/1-200W.csv',
         # '2000W/200W-400W.csv',
         # '2000W/400W-600W.csv',
         # '2000W/600W-800W.csv',
         # '2000W/800W-1000W.csv',
         # '2000W/1000W-1200W.csv',
         # '2000W/1200W-1400W.csv',
         # '2000W/1400W-1600W.csv',
         # '2000W/1600w-1800w.csv',
         # '2000W/1800w-2000w.csv',
         # '2000W/最后5000.csv'
         )
try:
    index = 0 #range:0~10
    buf = open(dataf[index])
    print 'open %s successfuly,start reading...' % dataf[index]
    content = buf.read()
finally:
    buf.close()
    print 'source closed,start processing...'
recs = content.split('\n')[1:-1]
# record counter
total = len(recs)
count = 0 

# 
try:
    password = getpass.getpass('Input password for the db:')
    conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd=password,db="data2000",charset='utf8')
    cur = conn.cursor()
    print 'Connected to db'

    patt = re.compile('\"[^"]*\"')

    try:    
        for i in range(len(recs)):
            record = recs[i]
            matchs = patt.findall(record)
            for match in matchs:
                record = record.replace(match,match.strip('"').replace(',','-'))
    #         record = re.sub(patt,recs[i].strip('"').replace(',','-'),recs[i])
            record = record.split(',')
    #         print len(record)
            if len(record) < 33:
                record = record + (33-len(record))*['']
            elif len(record) > 33:
                print 'warning:\n',record[0],record[7]
                opt = raw_input('record error:len>33.\n press q to quit,other keys to continue:')
                if opt=='q':
                    break
                else:
                    continue
            
            sql = 'INSERT INTO `hoteleak` (`Name`,`CardNo`,`Descriot`,`CtfTp`,`CtfId`,`Gender`,`Birthday`,`Address`,`Zip`,`Dirty`,\
            `District1`,`District2`,`District3`,`District4`,`District5`,`District6`,`FirstNm`,`LastNm`,`Duty`,`Mobile`,`Tel`,`Fax`,\
            `EMail`,`Nation`,`Taste`,`Education`,`Company`,`CTel`,`CAddress`,`CZip`,`Family`,`Version`,`Id`) \
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            
            param = record
    #         param = tuple(record)
            cur.execute(sql,param)
            
            count=count+1
            if count%10000==0:
                print count
            
    except Exception,e:
        conn.rollback()
        print str(e)
    else:
        conn.commit()
        print 'commited!'

finally:
    cur.close()
    conn.close()
    log = open('log.txt','a')
    log.write(time.ctime()+'--'+dataf[index]+'--counter:<'+str(count)+'/'+str(total)+'>records\n')
    log.close()
    print total,count,'mysql conn closed,over'
