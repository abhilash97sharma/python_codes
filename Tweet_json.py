#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
import socket
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "912719203689422854-eLrJkE92NdxG2IJuBdfCHbd8QRDi5J6"
access_token_secret = "DO281GcdPitM3Yhw8WPnt5MmOntFOj0Ykj2m95jW5ZTLO"
consumer_key = "tH2tCyRjkVq0KRcWAf2Ad8v8D"
consumer_secret = "KABoMkejFbbV0YKH7rBk33N6xwCfO7U77iu6kFLF0yptYmirKN"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        file = open('/home/abhilash/Desktop/tweet.txt', 'a')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = "192.168.1.8"
        port = 9999
        s.connect((ip, port))
        #print('Enter any string')
        # line = sys.stdin.readline()
        s.send(data.encode())

        file.write(str(data))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
   # print("hello")

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.filter(track='NarendraModi')