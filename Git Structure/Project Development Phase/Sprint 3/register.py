from flask import Flask,request,render_template
import ibm_db
from db import *
app = Flask(__name__)  
conn=ibm_db.connect(dbconnect(),"","") 


@app.route('/register',methods=['POST']) 
def register():
    print("checked")
    username=request.form['username']
    password=request.form['password']
    sql="SELECT * FROM user WHERE username=?"
    statement=ibm_db.prepare(conn,sql)
    ibm_db.bind_param(statement,1,username)
    ibm_db.execute(statement)
    acc=ibm_db.fetch_assoc(statement)
    if acc:
        "username already exists"
        return render_template("register.html")
    else:
        sql="INSERT INTO user(username,password) values(?,?)"
        statement=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(statement,1,username)
        ibm_db.bind_param(statement,2,password)
        ibm_db.execute(statement)
        print("created")
        return render_template("login.html")