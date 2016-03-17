#! /usr/bin/env python

__author__ = 'eason'

from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
        response=make_response('<h1>this document carries a cookie!</h1>')
        response.set_cookie('answer','42')
        return response

@app.route('/user/<name>')

def user(name):
        return '<h1>Hello world,%s!/<h1>' % name

if __name__=='__main__':
        app.run(debug=True)

