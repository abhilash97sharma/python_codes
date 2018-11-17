import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(('192.168.1.8',4444))
mysocket.listen(5)
(client,(ip,port)) = mysocket.accept()
client
#<socket._socketobject object at 0x7f7d6b62ade0>
ip
#'192.168.1.8'
port
#59810
client.send("hello abhilash")
#14
client.recv(2048)
#'Thanks for sending message'
client.close()



#import socket
#mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#mysocket.connect(('192.168.1.8',4444))
#data=mysocket.recv(1024)
#print data
#hello abhilash
#mysocket.send("Thanks for sending message")
#26
#mysocket.close()
