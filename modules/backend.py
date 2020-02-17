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
        try:
            mydb = mysql_con.connect()
            mycursor = mydb.cursor()
            data = request.get_json()
            sql = "INSERT INTO bukudetail (title, author, date_published, pages, type) VALUES (%s, %s, %s, %s, %s)"
            val = (data['title'], data['author'], data['date_published'], data['pages'], data['type'])
            mycursor.execute(sql, val)
            mydb.commit()
            message = 'success'
            fn = jsonify({'status': message})
        except:
            message = 'failed'
            fn = jsonify({'status': message})
        return fn

class update:
    def __init__(self):
        pass
    def update(data):
        try:
            mydb = mysql_con.connect()
            mycursor = mydb.cursor()
            data = request.get_json()
            sql = "UPDATE `bukudetail` SET `title` = '"+data['title']+"',`author` = '"+data['author']+"',`date_published` = '"+data['date_published']+"',`pages` = '"+data['pages']+"',`type` = '"+data['type']+"' WHERE `bukudetail`.`id` = '"+data['id']+"';"
            mycursor.execute(sql)
            mydb.commit()
            message = 'success'
            fn = jsonify({'status': message})
        except:
            message = 'failed'
            fn = jsonify({'status': message})
        return fn

class detailbook:
    def __init__(self):
        pass
    def detailbook(data):
        try:
            fx = []
            mydb = mysql_con.connect()
            mycursor = mydb.cursor()
            data = request.get_json()
            sql = "SELECT * FROM bukudetail WHERE id="+data['id']
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            for camp in myresult:
                dict_lat_cam_row = {
                    'id': camp[0],
                    'title': camp[1],
                    'author': camp[2],
                    'date_published': str(camp[3]),
                    'pages': camp[4],
                    'type': camp[5]
                }

            fx.append(dict_lat_cam_row)
            fn = jsonify({'hasil':fx})
        except:
            message = 'failed'
            fn = jsonify({'status': message})
        return fn


class delete:
    def __init__(self):
        pass
    def delete(data):
        try:
            mydb = mysql_con.connect()
            mycursor = mydb.cursor()
            data = request.get_json()
            d = data['id']
            sql = "DELETE FROM bukudetail where id="+ d
            mycursor.execute(sql)
            mydb.commit()
            message = 'success'
            fn = jsonify({'status': message})

        except:
            message = 'failed'
            fn = jsonify({'status': message})

        return fn
