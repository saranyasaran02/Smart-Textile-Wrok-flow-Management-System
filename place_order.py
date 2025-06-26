#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe

import os
import pymysql
import cgi
import cgitb

cgitb.enable()


con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()


form = cgi.FieldStorage()
uid = form.getvalue("id")
product_id = form.getvalue("product_id")
product_name = form.getvalue("product_name")
material = form.getvalue("material")
color = form.getvalue("color")
size = form.getvalue("size")
quantity = form.getvalue("quantity")
price = form.getvalue("price")

if all([uid, product_id, product_name, material, color, size, quantity, price]):
    total_price = int(quantity) * float(price)


    query = """
        INSERT INTO w_order
        (wholesaler_id, product_id, product_name, material, color, size, quantity, total_price, o_status,payment_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'ordered','Pending')
    """
    cur.execute(query, (uid, product_id, product_name, material, color, size, quantity, total_price))
    con.commit()

    print("Content-type:text/html\r\n\r\n")
    print("<script>alert('Order placed successfully!'); window.location.href='whole_sale.py?id=%s';</script>" % uid)
else:
    print("Content-type:text/html\r\n\r\n")
    print("<script>alert('Failed to place order. Please fill all fields.'); window.history.back();</script>")

con.close()
