from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import os
import ibm_db


DATABASE_NAME = "bludb"
HOST_NAME = "3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
PORT_NUMBER = "31498"
USER_ID = "qtl83809"
PASSWORD = "55UvDW1scUf5jZJn"


conn = ibm_db.connect(f"DATABASE={DATABASE_NAME};HOSTNAME={HOST_NAME};PORT={PORT_NUMBER};SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID={USER_ID};PWD={PASSWORD}",'','')


app = Flask(__name__)

@app.route('/')
def home():
    users = []
    sql = "SELECT * FROM user"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        # print ("The Name is : ",  dictionary)
        users.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if users:
        return render_template("index.html", users = users)
    else:
        return render_template("signup.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/adduser',methods = ['POST', 'GET'])
def adduser():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM user WHERE email =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('index.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO user VALUES (?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, password)
      ibm_db.execute(prep_stmt)
    
    return render_template('index.html', msg="Student Data saved successfuly..")

