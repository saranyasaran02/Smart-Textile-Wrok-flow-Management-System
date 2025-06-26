#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe

import os.path

print("content-type:text/html \r\n\r\n ")
import pymysql,cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="amazon")
cur=con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration form</title>
</head>
<style>

    *{
        font-family: 'Times New Roman', Times, serif;
    }
</style>

<body>
    <fieldset>
        <legend align="center">
            <h2>Admin Login Form</h2>
        </legend>
        <form method="post" enctype="multipart/form-data" name="register">

            
            <pre>Username                         <input type="text" name="uname"></pre><br>
            <pre>Password                          <input type="password" name="pass"></pre><br>
           
            <input type="submit" name="submit">

        </form>
    </fieldset>
</body>




</html>""")
form=cgi.FieldStorage()
id=form.getvalue("id")
user=form.getvalue("uname")
password=form.getvalue("pass")
submit=form.getvalue("submit")
if submit!=None:
    q="""select Id from admin where username='%s' and password='%s' """ %(user,password)
    cur.execute(q)
    res=cur.fetchone()
    if res !=None:
        print("""
        <script>
        alert("login success")
        location.href="admin_profile.py?id=%s"
        </script>
        
        """%(res[0]))
    else:
        print("""
        <script>
        alert("Incorrect password or user name")
        location.href="login2.py"
        </script>
        """)