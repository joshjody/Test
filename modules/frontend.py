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
        print(a1)
        fn = render_template("index.html",a1=a1)
        return fn
