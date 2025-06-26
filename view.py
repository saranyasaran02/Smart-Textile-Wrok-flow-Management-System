#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe

import os.path

print("content-type:text/html \r\n\r\n ")
import pymysql,cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="amazon")
cur=con.cursor()
form=cgi.FieldStorage()
x="""select * from customer"""
cur.execute(x)
res=cur.fetchall()
for i in res:
    print("""
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <img src="./images/%s">
    """ %(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10])

    )