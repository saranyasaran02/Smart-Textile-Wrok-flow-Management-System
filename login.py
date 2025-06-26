#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os.path

print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()

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
            <h2>Registration Form</h2>
        </legend>
        <form method="post" enctype="multipart/form-data" name="register">
           
            <pre>Id                         <input type="number" name="id"></pre><br>
            <pre>Username                         <input type="text" name="uname"></pre><br>
            <pre>Password                          <input type="password" name="pass"></pre><br>
            <pre>Fullname                         <input type="text" name="fname"></pre><br>
            <pre>Location                             <textarea name="address" rows="10" cols="30"></textarea><br>
            <pre>Upload Image                     <input type="file" name="image"></pre><br><br>
            <input type="submit" name="submit">

        </form>
    </fieldset>
</body>




</html>""")

form = cgi.FieldStorage()
id=form.getvalue("id")
fullname = form.getvalue("fname")
location = form.getvalue("address")
user = form.getvalue("uname")
password = form.getvalue("pass")
submit = form.getvalue("submit")
if submit != None:
    Image = form['image']
    fn = os.path.basename(Image.filename)
    open("images/" + fn, "wb").write(Image.file.read())

    x = """insert into admin(id,username,password,fullname,location,image)values('%s','%s','%s','%s','%s','%s')""" % (
    id,user,password,fullname,location,fn)
    cur.execute(x)
    con.commit()
    print("""

    <script>
    alert("Inserted successfully")
    </script>"""
          )