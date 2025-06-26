#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()

try:

    dealer_id = form.getvalue("dealer_id")
    payment_method = form.getvalue("payment_method")
    payment_details = form.getvalue("payment_details", "")

    if not dealer_id or not payment_method:
        raise Exception("Missing required fields")


    update_query = """UPDATE raw SET payment_status = 'Paid' WHERE rid = %s"""
    cur.execute(update_query, (payment_method, payment_details, dealer_id))
    con.commit()


    print("""
    <script>
        alert("Payment processed successfully!");
        window.location.href = "order_raw.py?dealer_id=""" + dealer_id + """";
    </script>
    """)

except Exception as e:

    print("""
    <script>
        alert("Error processing payment: """ + str(e) + """");
        window.history.back();
    </script>
    """)
finally:
    con.close()