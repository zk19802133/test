import os
def usbWalker(usbc,usbcfile):
    export = ""
    for root, dirs, files in os.walk(usbc):
        for dir in dirs:
            export += os.path.join(root,dir) + "\n"
        for file in files:
            export += os.path.join(root,file) + "\n"
    open(usbcfile, 'w').write(export)

if __name__ == '__main__':
    USB = 'i:\\'
    usbWalker(USB,"e:\\usbcheck.txt")
