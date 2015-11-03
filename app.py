#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

pages_list = ['zero','first','second']

@app.route('/')
def index():
    return '<h1>Welcome to my first flask project</h1>'



#app.route gives url at which fuction output is provided by flask server

@app.route('/pages/<int:id>')
def pages(id):
    return('<h1>Welcome to my first flask project</h1>'
           '<p>You are on: {0}</p>').format(pages_list[id])

if __name__ == '__main__':

#we put this in this if conditional because the flask webserver is not as
#good on production environment so we dont want app.run() in production
# to start the python webserver with debug arguments
    app.run(debug=True)
