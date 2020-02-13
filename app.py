import datetime
import mysql.connector
import sys

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import jsonify
from flask import make_response
from flask import render_template

from modules import mysql_con
from modules import frontend
from modules import backend


app = Flask(__name__)

#########################################################
#########################################################
####################### error 404 #######################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#########################################################
#########################################################
####################### backend #########################
@app.route('/v1/book/show', methods=['GET'])
def show():
    pro = backend.index().index()
    return pro
@app.route('/v1/book/add', methods=['POST'])
def add():
    pro = backend.add().add()
    return pro
@app.route('/v1/book/update', methods=['GET','POST'])
def update():
    pro = backend.index().index()
    return pro
@app.route('/v1/book/delete/<id>', methods=['GET','POST'])
def delete(id):
    pro = backend.index().index(id)
    return pro
#########################################################
#########################################################
####################### frontend ########################
@app.route('/', methods=['GET','POST'])
def index():
    pro = frontend.index().index()
    return pro

#########################################################
#########################################################
####################### debug on terminal ###############
if __name__ == '__main__':
   app.run(debug = True)
