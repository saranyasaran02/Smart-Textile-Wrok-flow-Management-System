#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe

import os.path

print("content-type:text/html \r\n\r\n ")
import pymysql,cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="amazon")
cur=con.cursor()
form=cgi.FieldStorage()
id=form.getvalue("id")
x="""select * from admin where id='%s' """ %(id)
cur.execute(x)
res=cur.fetchall()
for i in res:

    print("""
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <h1>%s</h1>
    <img src="./images/%s" height="150" width="150">
     """ %(i[0],i[1],i[2],i[3],i[4],i[5])
    )

    print("""
    <form>
    <input type="file" name="image">
    <input type="submit" value="Update" name="submit">
    </form>
    """)

    Submit=form.getvalue("submit")
    if Submit !=None:
        Image = form['image']
        fn = os.path.basename(Image.filename)
        open("images/" + fn, "wb").write(Image.file.read())
        q="""update admin set image='%s' where Id='%s' """ %(fn,id)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Updated Successfully")
        location.href="admin_profile.py?id='%s'"
        </script>
        """%(id))
