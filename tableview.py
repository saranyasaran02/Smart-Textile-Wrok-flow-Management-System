#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe

import  os.path
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
    <title>Document</title>
</head>
<body>
    <table border="1px" align="center" cellpadding="10px" cellspacing="3px" width="100%">
        <caption>Customer Data</caption><br>
        <tr>
            <th>
                Fullname
                

            </th>
            <th>
                Mail

            </th>
            <th>
                Phone

            </th>
            <th>
               Dob

            </th>
            <th>
                Gender

            </th>
            <th>
                State

            </th>
            <th>
                City

            </th>
            <th>
                Address

            </th>
            <th>
                Username

            </th>
            <th>
               Password

            </th>
            <th>
               Image

            </th>
            
        </tr>
    

""")

form=cgi.FieldStorage()
x="""select * from customer"""
cur.execute(x)
res=cur.fetchall()

for i in res:
    print("""
    
    <tr><td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src="./images/%s" width="100px" height="100px"></td></tr>
   
    
    """ %(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10] ))

print("""
    </table>
</body>
</html>
""")