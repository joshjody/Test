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
        fn = render_template("index.html",)
        return fn
