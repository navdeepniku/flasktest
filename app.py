#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my first flask project</h1>'

if __name__ == '__main__':

#we put this in this if conditional because the flask webserver is not as
#    good on production environment so we dont want app.run() in production
# to start the python webserver with debug arguments
    app.run(debug=True) 
