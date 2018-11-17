import socket
import sys

if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = "192.168.1.8"
    port = 9999
    s.connect((ip, port))
    print('Enter any string')
    #line = sys.stdin.readline()
    s.send(line.encode())

