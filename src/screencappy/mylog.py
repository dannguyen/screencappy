from sys import stdout, stderr

def myerr(*args):
    txt = ' '.join([str(a) for a in args])
    stderr.write(f'{txt}\n')

def mylog(*args):
    txt = ' '.join([str(a) for a in args])
    stdout.write(f'{txt}\n')
