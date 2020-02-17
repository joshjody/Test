import json
import mysql.connector
import requests
import os
import time
import sys
import datetime
import re
import random
from datetime import datetime,date


from flask import render_template_string
from flask import request
from flask import render_template
from flask import Flask
from flask import jsonify
from flask import session
from flask import make_response
from flask import redirect
from flask import url_for
from flask import send_from_directory



class index:
    def __init__(self):
        pass
    def index(self):
        url = 'http://127.0.0.1:5000/v1/book/show'
        y = requests.get(url)
        data = y.json()
        a1= data['buku']
        fn = render_template("index.html",a1=a1)
        return fn


class add:
    def __init__(self):
        pass
    def add(self):
        fn = render_template("tambah.html")
        return fn

class addproc:
    def __init__(self):
        pass
    def addproc(self):
        bookname    =   request.values.get('bookname')
        booktype    =   request.values.get('booktype')
        pages       =   request.values.get('pages')
        datep       =   request.values.get('datep')
        author      =   request.values.get('author')
        res = requests.post('http://127.0.0.1:5000/v1/book/add', json={"title":bookname,"author":author,"date_published":datep,"pages":pages,"type":booktype})
        fn = redirect('/')
        return fn

class delete:
    def __init__(self):
        pass
    def delete(self, params):
        idnya = params['id']
        res = requests.delete('http://127.0.0.1:5000/v1/book/delete', json={"id":idnya})
        fn = redirect('/')
        return fn
