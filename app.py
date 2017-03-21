'''
import requests
r = requests.get('https://api.github.com/events')
print (r.text)
'''
import socket
import datetime

from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def hello():
    '''
        hello
    '''
    return "Hello World! from " + socket.gethostname() + "  @  " + str(datetime.datetime.now())

if __name__ == "__main__":
    APP.run(host="0.0.0.0")
