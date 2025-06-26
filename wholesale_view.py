#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os
import sys

print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb
sys.stdout.reconfigure(encoding='utf-8')

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
l = """select * from wholesaler where id='%s' """ % (uid)
cur.execute(l)
rem = cur.fetchall()


o = """select w.wholesaler_id, w.product_id, w.product_name, w.material, w.size, w.color, w.quantity, w.total_price, w.o_status, w.payment_status 
       from w_order w where w.wholesaler_id='%s'""" % (uid)
cur.execute(o)
orders = cur.fetchall()

for i in rem:
    print("""
             <!DOCTYPE html>
             <html lang="en">

                 <head>
                     <meta charset="UTF-8">
                     <meta name="viewport" content="width=device-width, initial-scale=1.0">
                     <title>Wholesaler Dashboard</title>
                     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
                     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
                     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
                     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                     <style>
                         :root {
                             --primary-color: #eddacf;
                             --text-color: rgb(85, 77, 77);
                             --hover-color: rgba(0, 0, 0, 0.1);
                             --border-color: #ddd;
                             --shadow-color: rgba(0, 0, 0, 0.1);
                         }

                         body {
                             margin: 0;
                             padding: 0;
                             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                             background-color: #f8f9fa;
                             overflow-x: hidden; 
                         }

                         .sidebar {
                             background-color: var(--primary-color);
                             height: 100vh;
                             position: fixed;
                             width: 250px;
                             transition: all 0.3s ease;
                             padding-top: 20px;
                             left: 0;
                             z-index: 1000;
                             box-shadow: 2px 0 10px var(--shadow-color);
                         }

                         .sidebar h4 {
                             color: var(--text-color);
                             text-align: center;
                             margin-bottom: 30px;
                             font-weight: 600;
                             letter-spacing: 1px;
                         }

                         .sidebar .menu-item {
                             padding: 15px 20px;
                             color: var(--text-color);
                             cursor: pointer;
                             transition: all 0.3s ease;
                             display: flex;
                             align-items: center;
                             border-left: 4px solid transparent;
                             margin-bottom: 5px;
                         }

                         .sidebar .menu-item i {
                             margin-right: 15px;
                             font-size: 18px;
                             width: 20px;
                             text-align: center;
                         }

                         .sidebar .menu-item:hover {
                             font-weight: 600;
                             background-color: var(--hover-color);
                             transform: translateX(5px);
                         }

                         .content {
                             padding: 30px;
                             width: calc(100% - 250px); 
                             margin-left: 250px;
                             display: flex;
                             flex-direction: column;
                             align-items: center;
                             transition: all 0.3s ease;
                             box-sizing: border-box; 
                         }

                         .data-table {
                             width: 100%;
                             margin-top: 20px;
                             border-collapse: collapse;
                             box-shadow: 0 2px 10px var(--shadow-color);
                             background-color: white;
                             border-radius: 8px;
                             overflow: hidden;
                         }

                         .data-table th, .data-table td {
                             padding: 12px 15px;
                             text-align: left;
                             border-bottom: 1px solid var(--border-color);
                         }

                         .data-table th {
                             background-color: var(--primary-color);
                             color: var(--text-color);
                             font-weight: 600;
                         }

                         .data-table tr:hover {
                             background-color: #f5f5f5;
                         }

                         .status {
                             padding: 5px 10px;
                             border-radius: 20px;
                             font-size: 0.85em;
                             font-weight: 600;
                             display: inline-block;
                         }

                         .status.ordered {
                             background-color: #eddacf;
                             color:rgb(85, 77, 77) ;
                         }

                         .status.pending {
                             background-color: #fff8e7;
                             color: #cc8800;
                         }

                         .status.paid {
                             background-color: #e7ffe7;
                             color: #00cc00;
                         }

                         .btn-primary {
                             background-color: #6c5ce7;
                             border-color: #6c5ce7;
                             color: white;
                             transition: all 0.3s;
                         }

                         .btn-primary:hover {
                             background-color: #5649c0;
                             border-color: #5649c0;
                         }

                         .hamburger {
                             display: none;
                             position: fixed;
                             top: 15px;
                             left: 15px;
                             font-size: 24px;
                             cursor: pointer;
                             z-index: 1100;
                             background: var(--primary-color);
                             padding: 10px;
                             border-radius: 8px;
                             box-shadow: 0 2px 5px var(--shadow-color);
                         }

                         @media (max-width: 992px) {
                             .content {
                                 margin-left: 0;
                                 padding: 30px 15px;
                                 width: 100%;
                             }
                             .dealer-info {
                                 margin-left: 0 !important;
                                 padding: 20px !important;
                             }
                             .profile-card {
                                 width: 100% !important;
                                 max-width: 500px;
                             }
                         }

                         @media (max-width: 768px) {
                             .sidebar {
                                 left: -250px;
                                 width: 250px;
                             }
                             .content {
                                 margin-left: 0;
                                 padding: 30px 15px;
                                 padding-top: 80px;
                                 width: 100%;
                             }
                             .hamburger {
                                 display: block;
                             }
                             .sidebar.active {
                                 left: 0;
                             }
                             .page-title {
                                 margin-left: 0 !important;
                             }
                             .dealer-info {
                                 padding: 15px !important;
                             }
                             .info-row {
                                 flex-direction: column;
                                 align-items: flex-start !important;
                             }
                             .info-row .label {
                                 margin-bottom: 5px;
                             }
                         }


                         @media (min-width: 576px) {
                             .modal-dialog {
                                 max-width: 500px;
                             }
                         }
                     </style>
                 </head>""")
    print("""
               <body>
                   <div class="hamburger" id="toggleSidebar">
                       <i class="fa fa-bars"></i>
                   </div>

                   <div class="sidebar" id="sidebar">
                       <h4  style="margin-top:50px">Wholesaler Dashboard</h4><br>


                       <div class="menu-item">
                           <a href="wprofile.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                               <i class="fa-solid fa-user"></i> Profile
                           </a>
                       </div>
                       <div class="menu-item">
                           <a href="whole_sale.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                               <i class="fa-solid fa-shopping-cart"></i> Purchase Product
                           </a>
                       </div>


                       <div class="menu-item">
                           <a href="wholesale_view.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                               <i class="fa-solid fa-eye"></i>Purchased Product
                           </a>
                       </div>

                   </div>

                   <div class="content">
                         <h2 class="mb-4">Welcome %s</h2>

                         <div class="container-fluid">
                             <h4 class="mb-3">Your Ordered Products</h4>

                             <table class="data-table">
                                 <thead>
                                     <tr>
                                        
                                         <th>Product Name</th>
                                         <th>Material</th>
                                         <th>Size</th>
                                         <th>Color</th>
                                         <th>Quantity</th>
                                         <th>Total Price</th>
                                         <th>Order Status</th>
                                         <th>Payment Status</th>
                                         <th>Action</th>
                                     </tr>
                                 </thead>
                                 <tbody>
    """ % (uid, uid, uid, i[1]))


    for order in orders:
        payment_status = order[9]
        payment_button = ""


        if payment_status.lower() == "pending":
            payment_button = f"""
                        <a href="process_payment.py?id={uid}&product_id={order[1]}&order_id={order[0]}" class="btn btn-dark btn-sm">Pay Now</a>
                    """
        else:
            payment_button = "<span class='badge bg-success'>Paid</span>"

        print("""
                                    <tr>
                                        
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>%s</td>
                                        <td>₹%s</td>
                                        <td><span class="status ordered">%s</span></td>
                                        <td><span class="status %s">%s</span></td>
                                        <td>%s</td>
                                    </tr>
        """ % ( order[2], order[3], order[4], order[5], order[6], order[7], order[8],
               "pending" if payment_status.lower() == "pending" else "paid", payment_status, payment_button))

    print("""
                                </tbody>
                             </table>
                         </div>
                   </div>

                   <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
                   <script>
                       AOS.init({
                           duration: 1000,
                           easing: 'ease-in-out',
                           once: true
                       });

                       document.getElementById('toggleSidebar').addEventListener('click', function() {
                           document.getElementById('sidebar').classList.toggle('active');
                       });
                   </script>
               </body>
           </html>
    """)