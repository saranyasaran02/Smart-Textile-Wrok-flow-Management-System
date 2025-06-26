#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import sys
print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb, os
sys.stdout.reconfigure(encoding='utf-8')
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("dealer_id")

query = """SELECT * 
           FROM production 
           WHERE status = 'Ordered' and wid="%s" """ % (uid)
cur.execute(query)
ordered_products = cur.fetchall()

print("""
         <!DOCTYPE html>
         <html lang="en">

             <head>
                 <meta charset="UTF-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
                 <title>Admin Dashboard</title>

                 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
                 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
                 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
                 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                 <style>
                     :root {
                         --primary-color: #eddacf;
                         --text-color: rgb(85, 77, 77);
                         --hover-bg: rgba(0, 0, 0, 0.05);
                         --shadow-color: rgba(0, 0, 0, 0.1);
                     }

                     body {
                         margin: 0;
                         padding: 0;
                         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                         background-color: #f8f9fa;
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
                         font-weight: 600;
                         padding-bottom: 15px;
                         border-bottom: 1px solid rgba(85, 77, 77, 0.2);
                         margin: 0 20px 20px;
                     }

                     .sidebar .menu-item {
                         padding: 12px 25px;
                         color: var(--text-color);
                         cursor: pointer;
                         transition: all 0.2s ease;
                         display: flex;
                         align-items: center;
                         margin: 5px 0;

                     }

                     .sidebar .menu-item i {
                         margin-right: 15px;
                         width: 20px;
                         text-align: center;
                     }

                     .sidebar .menu-item:hover {
                         font-weight: 600;
                         background-color: var(--hover-bg);
                         transform: translateX(5px);
                     }

                     .sidebar .menu-item a {
                         text-decoration: none;
                         color: var(--text-color);
                         display: flex;
                         align-items: center;
                         width: 100%;
                     }

                     .dropdown-menu {
                         border: none;
                         box-shadow: 0 5px 15px var(--shadow-color);
                         border-radius: 10px;
                         padding: 10px 0;
                         margin-top: 10px;
                     }

                     .dropdown-item {
                         padding: 8px 20px;
                         transition: all 0.2s ease;
                     }

                     .dropdown-item:hover {
                         background-color: var(--primary-color);
                         transform: translateX(5px);
                     }

                     .content {
                        margin-left: 400px;
                        padding: 30px;
                        text-align: center;
                        max-width: 700px;
                        margin-right: auto;
                        transition: all 0.3s ease;
                    }

                    .profile-container {
                        background-color: var(--primary-color);
                        border-radius: 15px;
                        box-shadow: 0 5px 20px var(--shadow-color);
                        padding: 40px;
                        margin-top: 20px;
                        position: relative;
                        overflow: hidden;
                    }

                    .profile-header {
                        position: relative;
                        margin-bottom: 30px;
                    }



                    .profile-img-container {
                        position: relative;
                        display: inline-block;
                    }

                    .profile-img {
                        height: 150px;
                        width: 150px;
                        border-radius: 50%;
                        border: 5px solid white;
                        object-fit: cover;
                        box-shadow: 0 5px 15px var(--shadow-color);
                    }

                    .camera-icon {
                        position: absolute;
                        bottom: 15px;
                        right: 5px;
                        background-color: white;
                        border-radius: 50%;
                        padding: 8px;
                        box-shadow: 0 2px 8px var(--shadow-color);
                        cursor: pointer;
                        transition: all 0.2s ease;
                    }

                    .camera-icon:hover {
                        transform: scale(1.15);
                    }

                    .profile-details {
                        padding: 40px;
                    }

                    .profile-details h6 {
                        margin: 0;
                        color: var(--text-color);
                        font-weight: 600;
                    }




                    .profile-actions {
                        margin-top: 20px;
                    }

                    .btn-profile {
                        background-color: var(--text-color);
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 8px;
                        font-weight: 600;
                        margin: 0 10px;
                        transition: all 0.2s ease;
                    }

                    .btn-profile:hover {
                        transform: translateY(-3px);
                        box-shadow: 0 5px 15px var(--shadow-color);
                    }

                     .hamburger {
                         display: none;
                         position: fixed;
                         top: 15px;
                         left: 15px;
                         font-size: 20px;
                         cursor: pointer;
                         z-index: 1100;
                         background: var(--primary-color);
                         padding: 10px 12px;
                         border-radius: 8px;
                         box-shadow: 0 2px 10px var(--shadow-color);
                         color: var(--text-color);
                     }

                     .modal-content {
                         border-radius: 15px;
                         border: none;
                         box-shadow: 0 10px 30px var(--shadow-color);
                     }

                     .modal-header {
                         background-color: var(--primary-color);
                         border-radius: 15px 15px 0 0;
                         border-bottom: none;
                     }

                     .modal-body {
                         padding: 30px;
                     }

                     .form-control {
                         padding: 12px;
                         border-radius: 8px;
                         border: 1px solid #ced4da;
                         transition: all 0.2s;
                     }

                     .form-control:focus {
                         border-color: var(--text-color);
                         box-shadow: 0 0 0 0.25rem rgba(85, 77, 77, 0.25);
                     }

                     .btn-dark {
                         background-color: var(--text-color);
                         border: none;
                         padding: 10px 20px;
                         font-weight: 600;
                         border-radius: 8px;
                         transition: all 0.2s;
                     }

                     .btn-dark:hover {
                         background-color: rgba(85, 77, 77, 0.9);
                         transform: translateY(-2px);
                     }


                     .content-card {
                         background-color: white;
                         border-radius: 12px;
                         box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
                         padding: 25px;
                         margin-bottom: 30px;
                         width:1000px;
                     }

                     .content-header {
                         border-bottom: 1px solid #e9ecef;
                         padding-bottom: 15px;
                         margin-bottom: 20px;
                         text-align: left;
                     }

                     .content-header h2 {
                         color: #333;
                         font-weight: 600;
                         margin: 0;
                     }

                     .product-table {
                         width: 100%;
                         border-collapse: separate;
                         border-spacing: 0;
                     }

                     .product-table th,
                     .product-table td {
                         padding: 12px 15px;
                         text-align: left;
                         border-bottom: 1px solid #e9ecef;
                     }

                     .product-table th {
                         background-color: #f8f9fa;
                         color: #495057;
                         font-weight: 600;
                         font-size: 0.9rem;
                         text-transform: uppercase;
                         letter-spacing: 0.5px;
                     }

                     .product-table tr:last-child td {
                         border-bottom: none;
                     }

                     .product-table tr:hover {
                         background-color: #f8f9fa;
                     }

                     .btn-accept {
                         background-color: #28a745;
                         color: white;
                         border: none;
                         padding: 6px 15px;
                         border-radius: 5px;
                         font-weight: 500;
                         font-size: 0.85rem;
                         transition: all 0.2s;
                     }

                     .btn-accept:hover {
                         background-color: #218838;
                         transform: translateY(-2px);
                         box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                     }

                     .status-badge {
                         display: inline-block;
                         padding: 5px 10px;
                         border-radius: 30px;
                         font-size: 0.75rem;
                         font-weight: 600;
                         text-transform: uppercase;
                         letter-spacing: 0.5px;
                         background-color: #f8d7da;
                         color: #721c24;
                     }

                     @media (max-width: 992px) {
                         .sidebar {
                             left: -280px;
                             box-shadow: none;
                         }
                         .content {
                             margin-left: 0;
                             padding-top: 70px;
                             max-width: 100%;
                         }
                         .hamburger {
                             display: block;
                         }
                         .sidebar.active {
                             left: 0;
                             box-shadow: 2px 0 10px var(--shadow-color);
                         }
                     }

                     @media (max-width: 576px) {
                         .profile-actions {
                             display: flex;
                             flex-direction: column;
                             gap: 10px;
                         }

                         .btn-profile {
                             margin: 5px 0;
                         }
                     }
                 </style>
             </head>""")
print("""

           <body>
               <div class="hamburger" id="toggleSidebar">
                   <i class="fas fa-bars"></i>
               </div>

               <div class="sidebar" id="sidebar">
                   <h4 style="margin-top:50px">Owner Dashboard</h4>
                   <div class="menu-item">
                       <a href="oprofile.py?id=%s"><i class="fas fa-user-circle"></i> Profile</a>
                   </div>
                  <div class="menu-item">
                         <a href="order_raw.py?id=%s" ><i class="fas fa-box"></i> Dealer</a>

                   </div>
                   <div class="menu-item">
                       <a href="amanager.py?id=%s"><i class="fas fa-user-tie"></i> Manager</a>
                   </div>
                  <div class="menu-item">
                         <a href="adminwhole.py?id=%s"><i class="fas fa-box"></i> Wholesaler</a>

                   </div>

               </div>""" % (uid, uid, uid, uid))
print("""
    <div class="content" id="content" data-aos="fade-in">
        <div class="content-card">
            <div class="content-header">
                <h2><i class="fas fa-clipboard-list me-2"></i>Pending Orders</h2>
                <p class="text-muted mt-2 mb-0">Review and manage incoming product orders</p>
            </div>

            <div class="table-responsive">
                <table class="product-table">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Material</th>
                            <th>Size</th>
                            <th>Color</th>
                            <th>Quantity</th>
                            <th>Price (₹)</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
""")

for product in ordered_products:
    print(f"""
                <tr>
                    <td><strong>{product[1]}</strong></td>
                    <td>{product[2]}</td>
                    <td>{product[3]}</td>
                    <td>{product[4]}</td>
                    <td>{product[11]}</td>
                    <td>₹{product[12]}</td>
                    <form>
                    <td><input type="submit" class="btn-accept" {product[0]} name="oaccept" value="Accept"></td>
                    </form>
                </tr>
    """)

print("""
                    </tbody>
                </table>
            </div>
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
oaccept = form.getvalue("oaccept")
if oaccept != None:
    a = """update production set status="Accepted" where id="%s" """ % (query[0])
    cur.execute(a)
    con.commit()
    print("""
                   <script>
                   alert("Order Accepted !")
                   location.href="owholeview.py?id=%s"
                   </script>""" % (uid)
          )

    con.close()


