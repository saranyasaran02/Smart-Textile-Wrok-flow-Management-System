#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("id")
y = """select * from admin where Id="%s" """ % (id)
cur.execute(y)
res = cur.fetchall()
for i in res:


    print("""
         <!DOCTYPE html>
         <html lang="en">

             <head>
                 <meta charset="UTF-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
                 <title>Owner Dashboard</title>

                 
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
                        
                     }

                     .sidebar .menu-item a {
                         text-decoration: none;
                         color: var(--text-color);
                         display: flex;
                         align-items: center;
                         width: 100%;
                     }

                     
                     .content {
                        margin-left: 320px;
                        padding: 30px;
                        
                     }

                     .dealer-container {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: flex-start;
                        gap: 70px;
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


                    .dealer-card {
                        width: 330px;
                        border-radius: 15px;
                        overflow: hidden;
                        box-shadow: 0 5px 15px var(--shadow-color);
                        background-color: white;
                        margin-bottom: 30px;
                    }

                    .dealer-card:hover {
                       
                        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
                    }

                    .dealer-header {
                        background-color: var(--primary-color);
                        padding: 15px;
                        color: var(--text-color);
                        text-align: center;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }

                    .dealer-logo {
                        width: 60px;
                        height: 60px;
                        border-radius: 50%;
                        object-fit: cover;
                        border: 2px solid white;
                        margin-right: 15px;
                    }

                    .dealer-header-text {
                        text-align: left;
                    }

                    .dealer-header h4 {
                        margin: 0;
                        font-weight: 600;
                    }

                    .dealer-body {
                        padding: 20px;
                    }

                    .dealer-info {
                        margin-bottom: 15px;
                    }

                    .dealer-info i {
                        width: 20px;
                        color: var(--text-color);
                        margin-right: 10px;
                    }
                    .hed {
                         font-size: 25px;
                         color: var(--text-color);
                         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                         padding: 50px;
                         text-align:center;
                         margin-bottom:50px;
                    }
                    
                     .btn-dark {
                         background-color: var(--text-color);
                         border: none;
                         padding: 10px 20px;
                         font-weight: 600;
                         border-radius: 8px;
                         transition: all 0.2s;
                         width:50%;
                         
                         
                     }

                     .btn-dark:hover {
                         transform: translateY(-2px);
                     }
                    


                     @media (max-width: 992px) {
                         .sidebar {
                             left: -280px;
                             box-shadow: none;
                         }
                         .content {
                             margin-left: 0;
                             padding-top: 70px;
                         }
                         .hamburger {
                             display: block;
                         }
                         .sidebar.active {
                             left: 0;
                             box-shadow: 2px 0 10px var(--shadow-color);
                         }
                         .dealer-container {
                             justify-content: center;
                         }
                         .hed{
                             justify-content: center;
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
                .modal-content {
                    border-radius: 15px;
                    overflow: hidden;
                    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
                }
        
                .modal-header {
                    background-color: rgb(85, 77, 77);
                    border-bottom: none;
                    padding: 20px 25px;
                }
        
                .modal-title {
                    color: white;
                    font-weight: 600;
                    width: 100%;
                    text-align: center;
                    letter-spacing: 0.5px;
                }
        
                .modal-body {
                    padding: 30px;
                }
        
                .form-control {
                    border-radius: 8px;
                    padding: 12px 15px;
                    border: 1px solid var(--border-color);
                    transition: all 0.3s ease;
                    box-shadow: none;
                }
        
                .form-control:focus {
                    border-color: var(--accent-color);
                    box-shadow: 0 0 0 3px rgba(212, 168, 142, 0.2);
                }
        
                .form-label {
                    font-weight: 600;
                    color: var(--text-color);
                    margin-bottom: 8px;
                }
        
                .form-check-input:checked {
                    background-color: var(--accent-color);
                    border-color: var(--accent-color);
                }
        
                .color-option {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    margin-top: 10px;
                }
        
                .color-checkbox {
                    position: relative;
                    margin-bottom: 15px;
                }
        
                .color-checkbox input {
                    opacity: 0;
                    position: absolute;
                }
        
                .color-checkbox label {
                    display: inline-block;
                    padding: 8px 15px;
                    border-radius: 20px;
                    background-color: #f5f5f5;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    font-size: 14px;
                }
        
                .color-checkbox input:checked + label {
                    background-color: var(--accent-color);
                    color: white;
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
               </div>""" % (id, id, id,id))
print("""
               <div class="content" id="content">
                   <h6 class="hed">Dealer Details</h6>
                   <div class="dealer-container" >
                   """)

r = """select * from dealer where status="approved" """
cur.execute(r)
result = cur.fetchall()
for x in result:
        dealer_id=x[0]
        print("""
        
            <div class="dealer-card" >
                <div class="dealer-header">
                    <div class="dealer-logo-container">
                        <img src="./images/%s" class="dealer-logo" viewBox="0 0 100 100">
                    </div>
                    <div class="dealer-header-text">
                        <h4>%s</h4>
                        <small>Trusted Partner</small>
                    </div>
                </div>
                <div class="dealer-body">
                    <div class="dealer-info">
                        
                        <p><i class="fas fa-user"></i> Dealer: %s</p>
                        <p><i class="fas fa-phone"></i> Phone: %s</p>
                        <p><i class="fas fa-envelope"></i> Email: %s</p>
                        <p><i class="fas fa-map-marker-alt"></i> Location: %s</p>
                        <div class="d-flex">
                        <a href="purchase_raw.py?dealer_id=%s" class="btn btn-dark mt-4  mb-4 me-2" >View Product</a>
                        <a href="oraw_view.py?dealer_id=%s" class="btn btn-dark mt-4  mb-4" >View Order</a>
                        </div>  

                    </div>
                   

                
                 
        """ % (x[8],x[2], x[1], x[4], x[3], x[5],x[0],x[0]))



        print("""
                          
                    </div>
                </div>
        
               
                <script>
                
                document.getElementById('toggleSidebar').addEventListener('click', function() {
                document.getElementById('sidebar').classList.toggle('active');
                });
        
                </script>
        
        
               </body>
             </html>
         """)