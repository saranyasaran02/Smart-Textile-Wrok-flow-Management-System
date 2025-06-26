#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import random
import smtplib
import string

print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("id")
x = """select * from admin where id="%s" """ % (id)
cur.execute(x)
res = cur.fetchall()
for i in res:
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
                        margin-left: 550px;
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
                   <h4 style="margin-top:50px">Admin Dashboard</h4>
                   <div class="menu-item">
                       <a href="./aprofile.py?id=%s"><i class="fas fa-user-circle"></i> Profile</a>
                   </div>
                  <div class="menu-item">
                         <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown"><i class="fas fa-box"></i> Raw Material</a>
                         <ul class="dropdown-menu">
                         <li><a class="dropdown-item" href="./approve.py">Approve Dealer</a></li>
                         <li><a class="dropdown-item" href="#">Order Raw Material</a></li>
                         <li><a class="dropdown-item" href="#">View Dealers</a></li>
                         </ul>
                   </div>
                   <div class="menu-item">
                       <a href="./profile.html"><i class="fas fa-user-tie"></i> Manager</a>
                   </div>
                   <div class="menu-item">
                       <a href="./profile.html"><i class="fas fa-handshake"></i> Wholesalers</a>
                   </div>

               </div>""" % (id))
    print("""
           <div class="content" id="content">
               <h2 class="mb-4" style="color:var(--text-color); font-weight:600;margin-top:30px;">Welcome Admin</h2>
               <center><h2 class="mt-4">Dealer Information</h2></center><br>
    <table border="1px" align="center" cellpadding="10px" cellspacing="3px" width="100%" class="table-bordered">

        <tr>
            <th>
                Fullname


            </th>
            <th>
                Business Name

            </th>
            <th>
                Email

            </th>
            <th>
               Phone

            </th>
            <th>
                Location

            </th>
            <th>
                License No

            </th>
            <th>
                Raw Materials

            </th>
            <th>
                Authenticate

            </th>
        </tr>

""")
x = """select * from dealer where Status='false' """
cur.execute(x)
res = cur.fetchall()
for i in res:
    Name = i[1]
    Address = i[5]
    Email = i[3]
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><button type="button" class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#myModal%s">
    Open Modal</button></td>
    </tr>
    """ % (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[0])
          )


    def generate_random_string(length):
        characters = string.ascii_letters
        numbers = string.digits
        random_chars = random.choices(characters + numbers, k=length)
        return ''.join(random_chars)


    user_number = i[0]
    Gid = str(user_number)
    user_id = f"FK{user_number}"
    password = Name[0:2] + Address[1:4] + generate_random_string(2)
    print("""
    <div class="modal" id="myModal%s">
      <div class="modal-dialog">
        <div class="modal-content">

         
          <div class="modal-header">
            <h4 class="modal-title">Modal Heading</h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>

          
          <div class="modal-body">
            <form method="post">
            <input type="text" name="user_id" value="%s">
            <input type="text" name="password" value="%s">
            <input type="hidden" name="id" value="%s">

          </div>

         
          <div class="modal-footer">
            <input type="submit" class="btn btn-danger" value="update" name="update">
            </form>
          </div>

        </div>
      </div>
    </div>
    </div>""" % (i[0], user_id, password, i[0]))

    Cid = form.getvalue("id")
    User_id = form.getvalue("user_id")
    Password = form.getvalue("password")
    Submit = form.getvalue("update")
    if Submit != None:
        q = """update dealer set username='%s',Password='%s',Status="approved" where Id='%s'""" % (
        User_id, Password, Cid)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Password Updated Successfully")
        loctaion.href="approve.py"
        </script>
        """)
        print(
            """"

            </table>
            </body>
            </html>
            <script>
            alert("Mail sent Successfully");""")
        fromadd = 'saranyaselvan13@gmail.com'
        ppassword = 'ljmu vpta njtt sydn'
        toadd = Email
        subject = "Password From Floris knits"
        body = "hello:{} Your User Id is {} and  Password is {}".format(Name, User_id, Password)
        msg = """Subject:{} \n\n{}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd, ppassword)
        server.sendmail(fromadd, toadd, msg)
        server.quit()

