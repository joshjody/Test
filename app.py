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
@app.route('/v1/book/detailbook', methods=['GET'])
def detailbook():
    pro = backend.detailbook().detailbook()
    return pro
@app.route('/v1/book/add', methods=['POST'])
def add():
    pro = backend.add().add()
    return pro
@app.route('/v1/book/update', methods=['PUT'])
def update():
    pro = backend.update().update()
    return pro
@app.route('/v1/book/delete', methods=['GET','POST','DELETE'])
def delete():
    pro = backend.delete().delete()
    return pro
#########################################################
#########################################################
####################### frontend ########################
@app.route('/', methods=['GET','POST'])
def index():
    pro = frontend.index().index()
    return pro
@app.route('/addbook', methods=['GET','POST'])
def addfront():
    pro = frontend.add().add()
    return pro
@app.route('/tambah_proc', methods=['GET','POST'])
def tambah_procfront():
    pro     = frontend.addproc().addproc()
    return pro
@app.route('/delete/<id>', methods=['GET','POST'])
def delete_procfront(id):
    params = {"id" : id}
    pro = frontend.delete().delete(params)
    return pro
@app.route('/update/<id>', methods=['GET','POST'])
def updatefront(id):
    params = id
    pro = frontend.update().update(params)
    return pro
@app.route('/update_proc/<id>', methods=['GET','POST'])
def update_proc_front(id):
    params = id
    pro = frontend.update().update_proc(params)
    return pro
#########################################################
#########################################################
####################### debug on terminal ###############
if __name__ == '__main__':
   app.run(debug = True)
