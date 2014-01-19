from hashlib import md5

import os
 
def md5_file(name):
    m = md5()
    a_file = open(name, 'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
 
if __name__ == '__main__':
    file_list = {}
    while True:
        file_name = raw_input('Input file name or press ENTER\n>')
        if file_name:
            if os.path.isfile(file_name):
                file_list[file_name] = md5_file(file_name)
                print 'md5:',file_list[file_name]
            else:
                print 'File not exist!'
        else:
            break
    print 'Done'
