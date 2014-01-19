#-------------------------------------------------------------------------------
# Name:        scan_file
# Purpose:
#
# Author:      Administrator
#
# Created:     24-06-2013
# Copyright:   (c) Administrator 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# -*- coding: utf8 -*-
"""
ur"[\u3040-\u309F]+|[\u30A0-\u30FF]+|[\u31F0-\u31FF]+" Japanese
ur"[\u4e00-\u9fa5]+" Chinese,Japanese,Korean

"""
import os
import re

d=raw_input("input the path:").decode('utf-8')
if os.path.isdir(d):
    if not d.endswith('\\'):
        d=d+'\\'
    d=d.replace('/','\\')

    file_str=""
    counter=0
#   pattern=ur"[\u3040-\u309F]+|[\u30A0-\u30FF]+|[\u31F0-\u31FF]+"
    pattern=ur"[\u4e00-\u9fa5]+"
    print 'Scanning...'
    for root,rdir,rfile in os.walk(d):
        for r in rfile:
            if re.findall(pattern,r):
                file_str+=os.path.join(root,r)+'\n'
                counter+=1
    f=file('e:/scan_result.txt','a')
    f.write(file_str.encode('utf-8'))
    f.close()
    #print type(file_str.encode('utf-8'))
    #print file_str
    print 'Done: '+str(counter)+' records.'
else:
    print 'Invalid path.'

