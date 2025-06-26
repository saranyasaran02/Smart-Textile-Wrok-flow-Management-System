#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os
import os.path
import pymysql
import cgi
import cgitb

cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()

x = """SELECT * FROM dealer"""
cur.execute(x)
res = cur.fetchall()

if not res:
    print("content-type:text/html \r\n\r\n ")
    print("<script>alert('No data found');</script>")
    exit()

print("content-type:text/html \r\n\r\n ")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration form</title>
</head>
<style>
    * {
        font-family: 'Times New Roman', Times, serif;
    }
</style>

<body>
    <fieldset>
        <legend align="center">
            <h2>Registration Form</h2>
        </legend>
        <form method="post" enctype="multipart/form-data" name="register">
            <textarea></textarea><br>
            <input type="text" name="pid" value="%s">
            <pre>Upload Image                     <input type="file" name="image"></pre><br>
            <input type="submit" name="submit">
        </form>
    </fieldset>
</body>
</html>
""" % (res[0][0]))


form = cgi.FieldStorage()
proid = form.getvalue("pid")
submit = form.getvalue("submit")

if submit is not None:
    if "image" not in form or form['image'].filename == '':
        print("<script>alert('Please upload an image.');</script>")
    else:
        Image = form['image']
        fn = os.path.basename(Image.filename)


        if not os.path.exists("images"):
            os.makedirs("images")

        # Save the image
        with open("images/" + fn, "wb") as f:
            f.write(Image.file.read())

        # Update Database
        x = """UPDATE dealer SET liimage='%s' WHERE Id='65'""" % (fn)
        cur.execute(x)
        con.commit()

        print("<script>alert('Inserted successfully');</script>")
