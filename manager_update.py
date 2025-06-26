#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os

print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("id")
l = """select * from manager where id='%s' """ % (id)
cur.execute(l)
rem = cur.fetchall()
for i in rem:
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
                             --  shadow-color: rgba(0, 0, 0, 0.1);
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
                             margin-left: 150px;
                             display: flex;
                             flex-direction: column;
                             align-items: center;
                             transition: all 0.3s ease;
                             box-sizing: border-box; 
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

                         .profile-card {
                             background-color: var(--primary-color);
                             border-radius: 15px;
                             overflow: hidden;
                             box-shadow: 0 5px 15px var(--shadow-color);
                             transition: transform 0.3s ease;
                             width: 90%;
                             max-width: 600px;
                         }

                         .profile-header {
                             padding: 30px 0;
                             text-align: center;
                             position: relative;
                         }

                         .profile-image-container {
                             position: relative;
                             width: 150px;
                             height: 150px;
                             margin: 0 auto;
                         }

                         .profile-image {
                             width: 150px;
                             height: 150px;
                             border-radius: 50%;
                             object-fit: cover;
                             border: 4px solid white;
                             box-shadow: 0 4px 8px var(--shadow-color);
                         }

                         .camera-icon {
                             position: absolute;
                             bottom: 5px;
                             right: 5px;
                             background-color: white;
                             width: 40px;
                             height: 40px;
                             border-radius: 50%;
                             display: flex;
                             align-items: center;
                             justify-content: center;
                             cursor: pointer;
                             box-shadow: 0 2px 5px var(--shadow-color);
                             transition: all 0.3s ease;
                         }

                         .camera-icon:hover {
                             transform: scale(1.1);
                         }

                         .dealer-info {
                             padding: 20px 40px 30px;
                             width: 100%;
                             box-sizing: border-box;
                         }

                         .info-row {
                             display: flex;
                             padding: 12px 0;
                             border-bottom: 1px solid var(--border-color);
                             align-items: center;
                             flex-wrap: wrap; 
                         }

                         .info-row:last-child {
                             border-bottom: none;
                         }

                         .info-row .label {
                             font-weight: 600;
                             color: var(--text-color);
                             width: 120px;
                             text-align: left;
                             flex-shrink: 0;
                             display: flex;
                             align-items: center;
                         }

                         .info-row .label i {
                             margin-right: 10px;
                             width: 18px;
                             text-align: center;
                         }

                         .info-row .value {
                             color: #555;
                             text-align: left;
                             flex-grow: 1;
                             font-size: 16px;
                             word-break: break-word; 
                             max-width: 100%; 
                         }

                         .action-buttons {
                             padding: 15px 0;
                             display: flex;
                             justify-content: center;
                         }

                         .edit-btn {
                             background-color: var(--text-color);
                             color: white;
                             border: none;
                             padding: 10px 25px;
                             border-radius: 30px;
                             font-weight: 600;
                             transition: all 0.3s ease;
                             box-shadow: 0 3px 10px var(--shadow-color);
                         }

                         .edit-btn:hover {
                             transform: translateY(-3px);
                             box-shadow: 0 5px 15px var(--shadow-color);
                         }

                         .edit-btn i {
                             margin-right: 8px;
                         }

                         .page-title {
                             color: var(--text-color);
                             font-weight: 600;
                             margin-bottom: 30px;
                             text-align: center;
                             width: 100%;
                         }

                         .modal-content {
                             border-radius: 15px;
                             overflow: hidden;
                         }

                         .modal-header {
                             background-color: var(--primary-color);
                             border-bottom: none;
                             padding: 20px;
                         }

                         .modal-title {
                             color: var(--text-color);
                             font-weight: 600;
                             width: 100%;
                             text-align: center;
                         }

                         .modal-body {
                             padding: 30px;
                         }

                         .form-control {
                             border-radius: 8px;
                             padding: 12px;

                             border: 1px solid var(--border-color);
                         }

                         .btn-dark {
                             background-color: var(--text-color);
                             border: none;
                             border-radius: 30px;
                             padding: 10px 25px;
                             margin: 0 5px;
                             transition: all 0.3s ease;
                         }

                         .btn-dark:hover {
                             transform: translateY(-3px);
                             box-shadow: 0 5px 15px var(--shadow-color);
                         }


                         .modal-dialog {
                             max-width: 90%;
                             margin: 1.75rem auto;
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
                       <h4  style="margin-top:50px">Manager Dashboard</h4><br>


                       <div class="menu-item">
                           <a href="mprofile.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                               <i class="fa-solid fa-user"></i> Profile
                           </a>
                       </div>
                       <div class="menu-item">
                           <a href="manager_production.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                               <i class="fa-solid fa-shirt"></i> Production details
                           </a>
                       </div>


                       <div class="menu-item">
                           <a href="manager_update.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                               <i class="fa-solid fa-warehouse"></i>Finished Product
                           </a>
                       </div>


                   </div>

                    <div class="content" id="content">


                     
            </div>""" % (i[0], i[0], i[0]))
    print("""
               <script>
                   document.getElementById("toggleSidebar").addEventListener("click", function() {
                       document.getElementById("sidebar").classList.toggle("active");
                       document.getElementById("content").classList.toggle("sidebar-closed");
                   });
                   
               </script>
           </body>
         </html>
     """ )
