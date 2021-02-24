import os
from multiprocessing import Process

def run_func(name):
    print('child process %s(%s)' %(name,os.getpid()))

if __name__=='__main__':
    print('father process %s' %os.getpid())
    p=Process(target=run_func,args=('test',))
    print('child process starts')
    p.start()
    p.join()
    print('child process ends')
