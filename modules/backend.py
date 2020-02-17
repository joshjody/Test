import json
import mysql.connector
import requests
import os
import time
import sys
import datetime
import re
import random
from datetime import datetime

from flask import render_template_string
from flask import request
from flask import render_template
from flask import Flask
from flask import session
from flask import make_response
from flask import redirect
from flask import url_for
from flask import send_from_directory
from flask import jsonify

from modules import mysql_con


class index:
    def __init__(self):
        pass
    def index(self):
        mydb = mysql_con.connect()
        mycursor = mydb.cursor()
        book_all = []

        sql = "SELECT * FROM bukudetail"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            return book_all

        for book in myresult:
            dict_sub = {
            'id'                : book[0],
            'title'             : book[1],
            'author'            : book[2],
            'date_published'    : datetime.strptime(str(book[3]), '%Y-%m-%d').strftime('%d-%m-%Y'), #ganti format uy
            'pages'             : book[4],
            'type'              : book[5]
            }
            book_all.append(dict_sub)

        return jsonify({'buku': book_all}), 200 if book_all else 404

class add:
    def __init__(self):
        pass
    def add(data):
        # mydb = mysql_con.connect()
        # mycursor = mydb.cursor()
        try:
            # sql = "INSERT INTO bukudetail (title, author, date_published, pages, type) VALUES (%s, %s, %s, %s, %s)"
            # # val = (request['title'], request['author'], request['date_published'], request['pages'], request['type'])
            # val = (data['title'], data['author'], data['date_published'], data['pages'], data['type'])
            # print('asdasdasd')
            # mycursor.execute(sql, val)
            # mydb.commit()
            print("--------------1")
            mydb = mysql_con.connect()
            print("--------------2")
            mycursor = mydb.cursor()
            print("--------------3")
            sql = "INSERT INTO bukudetail (title, author, date_published, pages, type) VALUES (%s, %s, %s, %s, %s)"
            print("--------------4")
            val = (data['title'], data['author'], data['date_published'], data['pages'], data['type'])
            mycursor.execute(sql, val)
            mydb.commit()
            message = 'success'
            fn = jsonify({'status': message})

        except:
            message = 'failed'
            fn = jsonify({'status': message})

        return fn
