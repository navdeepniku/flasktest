#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

pages_list = ['zero','first','second']

@app.route('/')
def index():
    return render_template('index.html')



#app.route gives url at which fuction output is provided by flask server

@app.route('/pages/<int:id>')
def pages(id):
    return render_template('pages.html', page=pages_list[id])

if __name__ == '__main__':

#we put this in this if conditional because the flask webserver is not as
#good on production environment so we dont want app.run() in production
# to start the python webserver with debug arguments
    app.run(debug=True,host='0.0.0.0',port=80)
