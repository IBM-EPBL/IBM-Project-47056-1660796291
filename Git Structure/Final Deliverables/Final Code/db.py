from flask import Flask,render_template
import ibm_db

# conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCerficate=DigiCertGlobalRootCA.crt;UID=brl78982;PWD=pd6CRr0uGlvDjwVq",'  ',' ')

# print(conn)
# print("Connection Successful...")

# def dbconnect():
        
#     hostname="815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
#     uid="brl78982"
#     pwd="pd6CRr0uGlvDjwVq"
#     driver="{IBM DB2 ODBC DRIVER}"
#     db="bludb"
#     port="30367"
#     cert="DigiCertGlobalRootCA.crt"
#     dsn=(
#             "DATABASE={0};"
#             "HOSTNAME={1};"
#             "PORT={2};"
#             "UID={3};"
#             "SECURITY=SSL;"
#         "SSLServerCertificate={4};"
#         "PWD={5};"
         
#     ).format(db,hostname,port,uid,cert,pwd)
   
    
#     try:
#         db2=ibm_db.connect(dsn,"","")
#         print("connected")
#         return dsn
#     except:
#         print("unable to connect",ibm_db.conn_errormsg())
# import ibm_db
 
def dbconnect():
        
    hostname="815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
    uid="brl78982"
    pwd="pd6CRr0uGlvDjwVq"
    driver="{IBM DB2 ODBC DRIVER}"
    db="bludb"
    port="30367"
    cert="Certifiacte.crt"
    dsn=(
            "DATABASE={0};"
            "HOSTNAME={1};"
            "PORT={2};"
            "UID={3};"
            "SECURITY=SSL;"
        "SSLServerCertificate={4};"
        "PWD={5};"
         
    ).format(db,hostname,port,uid,cert,pwd)
    
    try:
        db2=ibm_db.connect(dsn,"","")
        print("connected")
        return dsn
    except:
        print("unable to connect",ibm_db.conn_errormsg())