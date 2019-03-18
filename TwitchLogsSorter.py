import time
import os

def lastline(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def UpdateLog(name,line):
    fil=open(name+'.txt','a')
    fil.write(line)
    fil.close()

def CreateLog(name,line):
    fil=open(name+'.txt','w')
    fil.write(line)
    fil.close()

if __name__=='__main__':
    tfile=os.getcwd()+'\\chat.log'
    logfile = open(tfile,'r')
    loglines = lastline(logfile)
    for line in loglines:
        if not line=='\n':
            username = line.split('--')[1].split(':')[0].strip(' ')
            if os.path.isfile('./'+username+'.txt')==True:
                UpdateLog(username,line)
            else:
                CreateLog(username,line)
