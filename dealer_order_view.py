#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")


print("""
         <!DOCTYPE html>
         <html lang="en">
             <head>
                 <meta charset="UTF-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
                 <title>Dealer Dashboard</title>
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
                         --accent-color: #d4a88e;
                         --card-bg: #ffffff;
                         --form-bg: #f8f9fa;
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
                         width: calc(100% - 250px); 
                         margin-left: 350px;
                         padding: 30px;
                         transition: all 0.3s ease;
                         box-sizing: border-box;
                         max-width: 900px;
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
                     }

                     
                     .page-title {
                         font-size: 1.8rem;
                         font-weight: 700;
                         color: var(--text-color);
                         margin-bottom: 25px;
                         padding-bottom: 15px;
                         border-bottom: 2px solid var(--accent-color);
                     }

                     .dashboard-card {
                         background-color: white;
                         border-radius: 12px;
                         box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                         margin-bottom: 25px;
                         overflow: hidden;
                         transition: all 0.3s ease;
                     }

                     .dashboard-card:hover {
                         box-shadow: 0 8px 25px rgba(0,0,0,0.12);
                         transform: translateY(-5px);
                     }

                     .card-header {
                         background-color: var(--primary-color);
                         padding: 18px 25px;
                         border-bottom: 1px solid var(--border-color);
                         display: flex;
                         align-items: center;
                         justify-content: space-between;
                     }

                     .card-title {
                         font-size: 1.4rem;
                         font-weight: 600;
                         color: var(--text-color);
                         margin: 0;
                         display: flex;
                         align-items: center;
                     }

                     .card-title i {
                         margin-right: 12px;
                         color: var(--text-color);
                         font-size: 1.5rem;
                     }

                     .card-body {
                         padding: 25px;
                     }

                     .product-status {
                         display: inline-block;
                         padding: 6px 15px;
                         border-radius: 20px;
                         font-weight: 600;
                         font-size: 0.85rem;
                         text-transform: uppercase;
                         letter-spacing: 0.5px;
                         background-color: var(--accent-color);
                         color: white;
                     }

                     .product-row {
                         display: flex;
                         align-items: center;
                         padding: 16px 0;
                         border-bottom: 1px solid rgba(0,0,0,0.06);
                     }

                     .product-row:last-child {
                         border-bottom: none;
                     }

                     .product-icon {
                         width: 45px;
                         height: 45px;
                         display: flex;
                         align-items: center;
                         justify-content: center;
                         background-color: rgba(212, 168, 142, 0.2);
                         border-radius: 10px;
                         margin-right: 20px;
                     }

                     .product-icon i {
                         color: var(--accent-color);
                         font-size: 1.3rem;
                     }

                     .product-details {
                         flex: 1;
                     }

                     .product-name {
                         font-weight: 600;
                         color: var(--text-color);
                         margin-bottom: 5px;
                         font-size: 1.05rem;
                     }

                     .product-spec {
                         color: #777;
                         font-size: 0.9rem;
                     }

                     .product-quantity {
                         font-weight: 600;
                         color: var(--accent-color);
                         font-size: 1.1rem;
                         text-align: right;
                         margin-left: 15px;
                     }

                     .total-section {
                         background-color: rgba(237, 218, 207, 0.2);
                         padding: 20px 25px;
                         border-radius: 10px;
                         margin-top: 15px;
                     }

                     .total-row {
                         display: flex;
                         justify-content: space-between;
                         align-items: center;
                         font-weight: 700;
                         color: var(--text-color);
                         font-size: 1.15rem;
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
                         transform: translateY(-2px);
                     }
                    
                     
                 </style>
             </head>""")
print("""
           <body>
          
               <div class="hamburger" id="toggleSidebar">
               
                   <i class="fa fa-bars"></i>
               </div>

               <div class="sidebar" id="sidebar">
                   <h4  style="margin-top:50px">Dealer Dashboard</h4><br>
                   
                   <div class="menu-item">
                       <a href="dprofile.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                           <i class="fa-solid fa-user"></i> Profile
                       </a>
                   </div>
                   <div class="menu-item">
                       <a href="dupdate.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                           <i class="fa-solid fa-box-open"></i> Product Update
                       </a>
                   </div>
                   <div class="menu-item">
                       <a href="rawview.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                           <i class="fa-solid fa-eye"></i> View Updated Product
                       </a>
                   </div>
                   

                   <div class="menu-item">
                       <a href="dealer_order_view.py ?id=%s" style="text-decoration: none;color:var(--text-color);">
                           <i class="fa-solid fa-shopping-cart"></i> View Orders
                       </a>
                   </div>
                   
               </div>""" % (uid, uid, uid, uid))

                

l = """select * from raw where rid="%s"  """ % (uid)
cur.execute(l)
res = cur.fetchall()
for r in res:
    print("""   
               
                    <div class ="content" id="content" >

                    <div class="dashboard-card">
                        <div class="card-header">
                            <h3 class="card-title">
                                <i class="fas fa-box-open"></i> Order Details
                            </h3>
                            <span class="product-status">%s</span>
                        </div>

                        <div class="card-body">
                            <div class="product-row">
                                <div class="product-icon">
                                    <i class="fas fa-cube"></i>
                                </div>
                                <div class="product-details">
                                    <div class="product-name">%s</div>
                                    <div class="product-spec">Specification: %s</div>
                                </div>
                            </div>

                            <div class="product-row">
                                <div class="product-icon">
                                    <i class="fas fa-cube"></i>
                                </div>
                                <div class="product-details">
                                    <div class="product-name">%s</div>
                                    <div class="product-spec">Specification: %s</div>
                                </div>
                            </div>

                            <div class="product-row">
                                <div class="product-icon">
                                    <i class="fas fa-cube"></i>
                                </div>
                                <div class="product-details">
                                    <div class="product-name">%s</div>
                                    <div class="product-spec">Specification: %s</div>
                                </div>
                            </div>
                            <div class="product-row">
                                <div class="product-icon">
                                    <i class="fa-solid fa-calendar-days"></i>
                                </div>
                                <div class="product-details">
                                    <div class="product-name">%s</div>
                                    
                                </div>
                            </div>

                            <div class="total-section">
                                <div class="total-row">
                                    <div>
                                        <i class="fas fa-weight-hanging"></i> Total Inventory Quantity:
                                    </div>
                                    <div>%s Units</div>
                                </div>
                            </div>
                            <center>
                            <form method="post" >
                            <input type="submit" class="btn btn-dark mt-4  mb-4" value="Accept Order" name="accept" >
                            <input type="hidden" name="mate" value="%s">
                           </form>
                           </center>
                        </div>
                        
                    </div>
                </div>
            """ % (r[13], r[14], r[17], r[15], r[18], r[16], r[19], r[24],r[20],r[2]))

    print("""
                    <script>
                        document.getElementById('toggleSidebar').addEventListener('click', function() {
                            document.getElementById('sidebar').classList.toggle('active');
                        });
                       
                    </script>
                </body>
            </html>
           """)



    order_accept = form.getvalue("accept")
    omat=form.getvalue("mate")
    if order_accept != None:
            a="""update raw set order_status="Order Accepted" where rid="%s" and material="%s" """ %(uid,omat)
            cur.execute(a)
            con.commit()
            print("""
        
                    <script>
                    alert("Order has been accepted!")
                     window.location.href = 'dealer_order_view.py?id=%s';
                    </script> """ %(uid))
