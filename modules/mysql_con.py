import mysql.connector

def connect():
    mydb = mysql.connector.connect(
      host="localhost",
      port=3306,
      user="root",
      passwd="",
      database="tokobukubambank"
    )
    return mydb
