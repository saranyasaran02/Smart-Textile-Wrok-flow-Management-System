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
            <h2>Registration Form</h2>
        </legend>
        <form method="post" enctype="multipart/form-data" name="register">
            <pre>Full Name                          <input type="text" name="fname"></pre><br>
            <pre>Email Address                   <input type="email" name="mail"></pre><br>
            <pre>Phone Number                   <input type="number" name="phno"></pre><br>
            <pre>Date Of Birth                      <input type="date" name="dob"></pre><br>
            <pre>Gender                             <input type="radio" name="gender" value="male">Male     <input type="radio" name="gender" value="female">Female
        </pre><br>
            <pre>State                                  <select name="state">
                <option selected disabled>Select Your State</option>
                <option value="Andhra Pradesh">Gujarat</option>
                <option value="Manipur">Manipur</option>
                <option value="Karnataka">Karnataka</option>
                <option value="Kerala">Kerala</option>
                <option value="Maharashtra">Maharashtra</option>
                <option value="Madhya Pradesh">Madhya Pradesh</option>
                <option value="Delhi">Delhi</option>
                <option value="Tamilnadu">Tamilnadu</option>
                    </select>
            </pre><br>
            <pre>City                                   <select name="city">
                <option selected disabled>Select Your City</option>
                <option value="Coimbatore">Coimbatore</option>
                <option value="Chennai">Chennai</option>
                <option value="Erode">Erode</option>
                <option value="Karur">Karur</option>
                <option value="Thanjavur">Thanjavur</option>
                <option value="Trichy">Trichy</option>
                <option value="Tiruppur">Tiruppur</option>
                <option value="Salem">Salem</option>
            </select></pre>   <br>
            <pre>Address                             <textarea name="address" rows="10" cols="30"></textarea><br>
            <pre>Upload Image                     <input type="file" name="image"></pre><br>
            <pre>Username                         <input type="text" name="uname"></pre><br>
            <pre>Password                          <input type="password" name="pass"></pre><br><br>
            <input type="submit" name="submit">

        </form>
    </fieldset>
</body>

</html>""")

form=cgi.FieldStorage()
fullname=form.getvalue("fname")
email=form.getvalue("mail")
phone=form.getvalue("phno")
date=form.getvalue("dob")
gender=form.getvalue("gender")
state=form.getvalue("state")
city=form.getvalue("city")
address=form.getvalue("address")
user=form.getvalue("uname")
password=form.getvalue("pass")
submit=form.getvalue("submit")
if submit!=None:
    Image=form['image']
    fn=os.path.basename(Image.filename)
    open("images/"+fn,"wb").write(Image.file.read())

    x="""insert into customer(fname,mail,phno,dob,gender,state,city,address,username,password,image)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(fullname,email,phone,date,gender,state,city,address,user,password,fn)
    cur.execute(x)
    con.commit()
    print("""
    <script>
    alert("Inserted successfully")
    </script>"""
    )