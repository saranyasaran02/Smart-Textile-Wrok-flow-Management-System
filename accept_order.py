#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
order_id = form.getvalue("order_id")
dealer_id = form.getvalue("dealer_id")


query = """UPDATE production SET status='Accepted' WHERE id=%s"""
cur.execute(query, (order_id,))
con.commit()

print("Order accepted successfully!")