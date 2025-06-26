#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb, os
import random
import smtplib
import string

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
Id = form.getvalue("id")

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
                         overflow-y: auto;
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
                        margin-left: 250px;
                        padding: 30px;
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


                     .dealer-table-wrapper {
                         width: 100%;
                         overflow-x: auto;
                         -webkit-overflow-scrolling: touch;
                         margin-bottom: 20px;
                         border-radius: 12px;
                         box-shadow: 0 5px 15px var(--shadow-color);
                     }

                     .dealer-table {
                         border-collapse: separate;
                         border-spacing: 0;
                         width: 100%;
                         background-color: white;
                         min-width: 800px; /* Ensures table doesn't get too compressed */
                     }

                     .dealer-table th {
                         background-color: var(--primary-color);
                         color: var(--text-color);
                         font-weight: 600;
                         text-align: left;
                         padding: 15px;
                         font-size: 14px;
                         letter-spacing: 0.5px;
                         border: none;
                         position: sticky;
                         top: 0;
                     }

                     .dealer-table td {
                         padding: 12px 15px;
                         border-bottom: 1px solid rgba(0,0,0,0.05);
                         color: var(--text-color);
                         font-size: 14px;
                         vertical-align: middle;
                     }

                     .dealer-table tr:last-child td {
                         border-bottom: none;
                     }

                     .dealer-table tr:hover td {
                         background-color: rgba(237, 218, 207, 0.1);
                     }


                     .modal-content {
                         border-radius: 15px;
                         border: none;
                         box-shadow: 0 10px 30px var(--shadow-color);
                         overflow: hidden;
                     }

                     .modal-header {
                         background-color: var(--primary-color);
                         border-radius: 15px 15px 0 0;
                         border-bottom: none;
                         padding: 20px 25px;
                     }

                     .modal-header h4 {
                         color: var(--text-color);
                         font-weight: 600;
                         margin: 0;
                     }

                     .modal-body {
                         padding: 25px;
                     }

                     .form-group {
                         margin-bottom: 20px;
                     }

                     .form-label {
                         color: var(--text-color);
                         font-weight: 500;
                         margin-bottom: 8px;
                         display: block;
                     }

                     .form-control {
                         padding: 12px 15px;
                         border-radius: 8px;
                         border: 1px solid rgba(0,0,0,0.1);
                         transition: all 0.3s;
                         width: 100%;
                         font-size: 14px;
                         color: var(--text-color);
                         background-color: #f9f9f9;
                     }

                     .form-control:focus {
                         border-color: var(--primary-color);
                         box-shadow: 0 0 0 3px rgba(237, 218, 207, 0.25);
                         outline: none;
                     }

                     .modal-footer {
                         border-top: none;
                         padding: 15px 25px 25px;
                     }

                     .btn-action {
                         background-color: var(--text-color);
                         color: white;
                         border: none;
                         padding: 10px 20px;
                         border-radius: 8px;
                         font-weight: 600;


                     }

                     .btn-action:hover {

                        background-color: var(--primary-color);
                        color: var(--text-color);

                     }

                     .section-header {
                         color: var(--text-color);
                         font-weight: 600;
                         margin-bottom: 30px;
                         padding-bottom: 15px;
                         border-bottom: 2px solid var(--primary-color);
                         display: inline-block;
                     }

                     .page-container {
                         background-color: white;
                         border-radius: 15px;
                         box-shadow: 0 5px 20px var(--shadow-color);
                         padding: 30px;
                         margin-bottom: 30px;
                     }


                     @media (max-width: 1200px) {
                         .content {
                             padding: 20px;
                         }
                     }

                     @media (max-width: 992px) {
                         .sidebar {
                             left: -250px;
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
                         .page-container {
                             padding: 20px;
                         }
                     }

                     @media (max-width: 768px) {
                         .content {
                             padding: 70px 15px 15px;
                         }
                         .page-container {
                             padding: 15px;
                         }
                         .section-header {
                             font-size: 1.5rem;
                         }
                         .dealer-table th, .dealer-table td {
                             padding: 10px;
                             font-size: 13px;
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
                         .page-container {
                             padding: 12px;
                         }
                         .btn-action {
                             padding: 8px 12px;
                             font-size: 12px;
                         }
                         .dealer-table th, .dealer-table td {
                             padding: 8px;
                             font-size: 12px;
                         }
                     }

                     .back-to-top {
                         position: fixed;
                         bottom: 20px;
                         right: 20px;
                         background-color: var(--primary-color);
                         color: var(--text-color);
                         width: 40px;
                         height: 40px;
                         border-radius: 50%;
                         display: flex;
                         align-items: center;
                         justify-content: center;
                         cursor: pointer;
                         box-shadow: 0 2px 10px var(--shadow-color);
                         opacity: 0;
                         visibility: hidden;
                         transition: all 0.3s;
                     }

                     .back-to-top.visible {
                         opacity: 1;
                         visibility: visible;
                     }

                     .back-to-top:hover {
                         transform: translateY(-3px);
                     }
                 </style>
             </head>""")
l = """select * from admin where Id='%s' """ % (Id)
cur.execute(l)
rem = cur.fetchall()
for d in rem:
    print("""

           <body>
               <div class="hamburger" id="toggleSidebar">
                   <i class="fas fa-bars"></i>
               </div>

               <div class="sidebar" id="sidebar">
                   <h4 style="margin-top:50px">Admin Dashboard</h4>
                   
                  <div class="menu-item">
                         <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown"><i class="fas fa-box"></i>Dealer</a>
                         <ul class="dropdown-menu">
                         <li><a class="dropdown-item" href="approve.py?id=%s">New Dealer</a></li>
                         <li><a class="dropdown-item" href="doriginal.py?id=%s">Approved Dealer</a></li>
                         <li><a class="dropdown-item" href="rejected.py?id=%s">Rejected Dealer
                         </a></li>
                         </ul>
                   </div>
                   
                   <div class="menu-item">
                         <a href="#" class="dropdown-toggle" data-bs-toggle="dropdown"><i class="fas fa-box"></i> Wholesaler</a>
                         <ul class="dropdown-menu">
                         <li><a class="dropdown-item" href="wapprove.py?id=%s">New Wholesaler</a></li>
                         <li><a class="dropdown-item" href="wdoriginal.py?id=%s">Approved Wholesaler</a></li>
                         <li><a class="dropdown-item" href="wrejected.py?id=%s">Rejected Wholesaler</a></li>
                         </ul>
                   </div>

               </div>""" % (d[0], d[0], d[0], d[0],d[0],d[0]))
    print("""
           <div class="content" id="content">
               <div class="page-container">
                   <h2 class="section-header">Approved Wholesaler</h2>


                   <div class="dealer-table-wrapper">
                       <table class="dealer-table">
                           <thead>
                               <tr>
                                   <th>Full Name</th>
                                   <th>Business Name</th>
                                   <th>Email</th>
                                   <th>Phone</th>
                                   <th>Location</th>
                                   <th>License No</th>
                                   <th>Logo</th>
                                   <th>License </th>
                                   <th>Actions</th>
                               </tr>
                           </thead>
                           <tbody>
        """)


def generate_random_string(length):
    characters = string.ascii_letters
    numbers = string.digits
    random_chars = random.choices(characters + numbers, k=length)
    return ''.join(random_chars)


x = """select * from wholesaler where status='approved' """
cur.execute(x)
res = cur.fetchall()
for i in res:
    dealer_id = i[0]
    Name = i[1]
    Address = i[5]
    Email = i[3]

    user_id = f"FK{dealer_id}"
    password = Name[0:2] + Address[1:4] + generate_random_string(2)

    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src="./images/%s" width="100px" height="100px"></td>
    <td><img src="./images/%s" width="100px" height="100px"></td>

    """ % (i[1], i[2], i[3], i[4], i[5], i[6], i[10],i[11]))

    print("""
     <td><button type="button" class="btn btn-action" data-bs-toggle="modal" data-bs-target="#myModal%s">
     <i class="fas fa-check-circle me-2"></i>Reject</button>

    <div class="modal" id="myModal%s">
      <div class="modal-dialog">
        <div class="modal-content">

          <!-- Modal Header -->
          <div class="modal-header">
            <h4 class="modal-title">Reject Wholesaler: %s</h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>

          <!-- Modal body -->
          <div class="modal-body">
            <form method="post">

              <p class="text-muted mt-3">These credentials will be sent to the dealer's email upon approval.</p>
              <input type="hidden" name="email" value="%s">
              <input type="hidden" name="name" value="%s">
              <input type="hidden" name="dealer_id" value="%s">
          </div>

          <!-- Modal footer -->
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <input type="submit" class="btn btn-action" value="Confirm Rejection" name="update">
            </form>
          </div>

        </div>
      </div>
    </div>

        """ % (dealer_id, dealer_id, i[1], i[3], i[1], dealer_id))

print(""" 
                           </tbody>
                       </table>
                   </div>
               </div>

               <!-- Back to top button -->
               <div class="back-to-top" id="backToTop">
                   <i class="fas fa-arrow-up"></i>
               </div>

               <script>

                   document.getElementById('toggleSidebar').addEventListener('click', function() {
                       document.getElementById('sidebar').classList.toggle('active');
                   });


                   const backToTopButton = document.getElementById('backToTop');

                   window.addEventListener('scroll', () => {
                       if (window.pageYOffset > 300) {
                           backToTopButton.classList.add('visible');
                       } else {
                           backToTopButton.classList.remove('visible');
                       }
                   });

                   backToTopButton.addEventListener('click', () => {
                       window.scrollTo({
                           top: 0,
                           behavior: 'smooth'
                       });
                   });


                   document.addEventListener('click', function(event) {
                       const sidebar = document.getElementById('sidebar');
                       const toggleButton = document.getElementById('toggleSidebar');

                       if (window.innerWidth <= 992 && 
                           !sidebar.contains(event.target) && 
                           !toggleButton.contains(event.target) &&
                           sidebar.classList.contains('active')) {
                           sidebar.classList.remove('active');
                       }
                   });
               </script>
           </div>
        </body>
        </html>""")

User_id = form.getvalue("user_id")
Email = form.getvalue("email")
Name = form.getvalue("name")
Password = form.getvalue("password")
dealer_id = form.getvalue("dealer_id")
Submit = form.getvalue("update")

rejid = form.getvalue("rejid")
rejsubmit = form.getvalue("reject")

if Submit != None:

    a = """update wholesaler set status="rejected",username='',password='' where Id='%s' """ % (dealer_id)
    cur.execute(a)
    con.commit()

    fromadd = 'saranyaselvan13@gmail.com'
    ppassword = 'ljmu vpta njtt sydn'
    toadd = Email
    subject = "Application Status From Floris knits"
    body = "hello:{} Your applicaation is rejected upon invalid credentials.".format(Name)
    msg = """Subject:{} \n\n{}""".format(subject, body)

    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd, ppassword)
        server.sendmail(fromadd, toadd, msg)
        server.quit()

        print("""
        <script>
        alert("Dealer rejected and email sent successfully!");
        window.location.href = "wdoriginal.py?id=%s";
        </script>
        """ % (Id))
    except Exception as e:
        print("""
        <script>
        alert("Error sending email: %s");
        window.location.href = "wdoriginal.py?id=%s";
        </script>
        """ % (str(e), Id))