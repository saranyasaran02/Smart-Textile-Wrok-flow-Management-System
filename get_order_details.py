#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import sys
import pymysql
import cgi
import cgitb

cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')


form = cgi.FieldStorage()
dealer_id = form.getvalue("dealer_id")

con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()


if "acc" in form:
    product_id = form.getvalue("product_id")
    wholesaler_id = form.getvalue("wholesaler_id")


    try:

        if not product_id or not wholesaler_id:
            raise ValueError("Invalid product ID or wholesaler ID.")


        update_query = """
            UPDATE w_order 
            SET o_status='Accepted' 
            WHERE wholesaler_id=%s AND product_id=%s AND o_status='ordered' 
        """
        cur.execute(update_query, (wholesaler_id, product_id))
        affected_rows = cur.rowcount
        con.commit()


        print("content-type:text/html \r\n\r\n")

        if affected_rows > 0:
            print(f"""
            <script>
            alert("Order accepted successfully!");
            
            </script>
            """)
        else:
            print(f"""
            <script>
            alert("It may have already been accepted .");
            history.back();
            </script>
            """)
    except Exception as e:

        print("content-type:text/html \r\n\r\n")
        print(f"""
        <script>
        alert("Error: {str(e)}");
        window.location.href = "adminwhole.py?id=1";
        </script>
        """)
    finally:

        if "acc" in form:
            cur.close()
            con.close()
            sys.exit()
else:

    print("content-type:text/html \r\n\r\n")


if "acc" not in form:
    try:

        if not dealer_id:
            print("<h2>Error: Missing dealer ID</h2>")
            cur.close()
            con.close()
            sys.exit()


        query = "SELECT * FROM w_order WHERE  wholesaler_id = %s  "
        cur.execute(query, (dealer_id,))
        ordered_products = cur.fetchall()

        print("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Wholesaler Orders</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                h1 {
                    color: #333;
                }
                .product-table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                .product-table th {
                    background-color: #f2f2f2;
                    font-weight: bold;
                }
                .product-table th, .product-table td {
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: left;
                }
                .product-table tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                .btn-success {
                    background-color: #5cb85c;
                    color: white;
                    padding: 5px 10px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                .btn-success:hover {
                    background-color: #4cae4c;
                }
            </style>
        </head>
        <body>
            
            <div class="table-responsive">
                <table class="product-table">
                    <thead>
                        <tr>
                            <th>Product Name</th>
                            <th>Material</th>
                            <th>Size</th>
                            <th>Color</th>
                            <th>Quantity</th>
                            <th>Price (₹)</th>
                            <th>Status</th>
                            <th>Payment Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
        """)


        for product in ordered_products:
            print(f"""
                <tr>
                    <td><strong>{product[2]}</strong></td>
                    <td>{product[3]}</td> 
                    <td>{product[4]}</td> 
                    <td>{product[5]}</td>
                    <td>{product[6]}</td> 
                    <td>₹{product[7]}</td>
                    <td>{product[8]}</td>
                    <td>{product[9]}</td>
                    <td>
                        <form method="post" action="get_order_details.py">
                            <input type="hidden" name="product_id" value="{product[1]}">
                            <input type="hidden" name="wholesaler_id" value="{product[0]}">
                            <input type="hidden" name="dealer_id" value="{dealer_id}">
                            <input type="submit" name="acc" value="Accept" class="btn-success">
                        </form>
                    </td>
                </tr>
            """)


        if len(ordered_products) == 0:
            print("""
                <tr>
                    <td colspan="10" style="text-align: center;">No pending orders found</td>
                </tr>
            """)

        print("""
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """)
    except Exception as e:
        print(f"<h2>Error: {str(e)}</h2>")
    finally:

        cur.close()
        con.close()