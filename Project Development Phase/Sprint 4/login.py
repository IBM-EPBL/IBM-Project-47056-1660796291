# from flask import Flask,render_template,request
# import ibm_db
# from db import *
# app = Flask(__name__)  
# #conn=ibm_db.connect(dbconnect(),"","")   

# @app.route('/') 
# def login():  
#     return render_template("login.html")
# msg=""
# @app.route('/upload', methods=['POST']) 
# def upload():
    
    
#      username=request.form['username']
     
#      password=request.form['password']
#      sql="SELECT * FROM USERS WHERE username=? AND password=?"
#      statement=ibm_db.prepare(conn,sql)
#      ibm_db.bind_param(statement,1,username)
#      ibm_db.bind_param(statement,2,password)
#      ibm_db.execute(statement)
#      acc=ibm_db.fetch_assoc(statement)
#      if acc:
#         return render_template("newspage.html")
#      else:
#         msg="Invalid username or password"
#         return render_template("login.html")

# @app.route('/signup',methods=['GET'])
# def signup():
#     return render_template("register.html")

# @app.route('/register',methods=['POST'])
# def register():
#     print("checked")
#     username1=request.form['username']
#     password1=request.form['password']
#     sql="SELECT * FROM USERS WHERE username=?"
#     statement=ibm_db.prepare(conn,sql)
#     ibm_db.bind_param(statement,1,username1)
#     ibm_db.execute(statement)
#     acc=ibm_db.fetch_assoc(statement)
#     if acc:
#         print("username already exists")
#         return render_template("register.html") 
#     else:
#         sql="INSERT INTO USERS(username,password) values(?,?)"
#         statement=ibm_db.prepare(conn,sql)
#         ibm_db.bind_param(statement,1,username1)
#         ibm_db.bind_param(statement,2,password1)
#         ibm_db.execute(statement)
#         print("created")
#         return render_template("login.html")
        

        

    


# if __name__ =='__main__':  
#     app.run(debug = True)  
from flask import Flask,render_template,request
import ibm_db
from db import *
from news import *
app = Flask(__name__)    
conn=ibm_db.connect(dbconnect(),"","") 
@app.route('/') 
def login():  
    return render_template("login.html")
msg=""
@app.route('/upload', methods=['POST']) 
def upload():
    
    
     username=request.form['username']
     
     password=request.form['password']
     sql="SELECT * FROM user WHERE username=? AND password=?"
     statement=ibm_db.prepare(conn,sql)
     ibm_db.bind_param(statement,1,username)
     ibm_db.bind_param(statement,2,password)
     ibm_db.execute(statement)
     acc=ibm_db.fetch_assoc(statement)
     if acc:
         return getnews()
     else:
        msg="Invalid username or password"
        return render_template("login.html")

@app.route('/signup',methods=['GET'])
def signup():
    return render_template("register.html")

@app.route('/register',methods=['POST'])
def register():
    print("checked")
    username1=request.form['username']
    password1=request.form['password']
    sql="SELECT * FROM user WHERE username=?"
    statement=ibm_db.prepare(conn,sql)
    ibm_db.bind_param(statement,1,username1)
    ibm_db.execute(statement)
    acc=ibm_db.fetch_assoc(statement)
    if acc:
        print("username already exists")
        return render_template("register.html") 
    else:
        sql="INSERT INTO user(username,password) values(?,?)"
        statement=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(statement,1,username1)
        ibm_db.bind_param(statement,2,password1)
        ibm_db.execute(statement)
        print("created")
        return render_template("login.html")
        
@app.route('/news')
def news():
     getnews()
       

    


if __name__ =='__main__':  
    app.run(debug = True)  
