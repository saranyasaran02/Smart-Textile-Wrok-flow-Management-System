#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("id")
x = """select * from admin where Id="%s" """ % (id)
cur.execute(x)
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
                        color:black;
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
                    }

                    .btn-profile:hover {
                        transform: scale(1.05);
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
                         transform: translateY(-2px);
                     }

                   
                     .password-container {
                         position: relative;
                     }

                     .password-toggle {
                         position: absolute;
                         right: 10px;
                         top: 50%;
                         transform: translateY(-50%);
                         cursor: pointer;
                         color: var(--text-color);
                         z-index: 10;
                     }

                     .password-toggle:hover {
                         color: #333;
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
                   <h4 style="margin-top:50px">Owner Dashboard</h4>
                   <div class="menu-item">
                       <a href="./oprofile.py?id=%s"><i class="fas fa-user-circle"></i> Profile</a>
                   </div>
                  <div class="menu-item">
                         <a href="order_raw.py?id=%s" ><i class="fas fa-box"></i>Dealer</a>
                        
                   </div>
                   <div class="menu-item">
                       <a href="amanager.py?id=%s"><i class="fas fa-user-tie"></i> Manager</a>
                   </div>
                   <div class="menu-item">
                         <a href="adminwhole.py?id=%s" ><i class="fas fa-box"></i> Wholesaler</a>
                        
                   </div>

               </div>""" % (i[0], i[0], i[0],i[0]))
    print("""
           <div class="content" id="content">
               <h2 class="mb-4" style="color:var(--text-color); font-weight:600;margin-top:30px;">Owner Profile</h2><br>

               <div class="profile-container">
                   <div class="profile-header">
                       <div class="profile-bg"></div>
                       <div class="profile-img-container">
                           <img src="./images/%s" class="profile-img" alt="Profile Image">
                           <a href="" data-bs-toggle="modal" data-bs-target="#imgModal" class="camera-icon">
                               <i class="fas fa-camera" style="color:var(--text-color);"></i>
                           </a>
                       </div>
                   </div>

                   <div class="profile-details">
                       <h6><i class="fas fa-user me-2"></i>%s</h6><br>
                       <h6><i cla

                       ss="fas fa-map-marker-alt me-2"></i>%s</h6><br>
                       <h6>
                           <i class="fas fa-crown me-2"></i>Owner
                       <h6><br>

                       <div class="profile-actions">
                           <button class="btn btn-profile" data-bs-toggle="modal" data-bs-target="#editModal">
                               <i class="fas fa-user-edit me-2"></i>Edit Profile Data
                           </button>
                           <button class="btn btn-profile" data-bs-toggle="modal" data-bs-target="#changeModal">
                               <i class="fas fa-key me-2"></i>Change Password
                           </button>
                       </div>
                   </div>
               </div>


               <div class="modal fade" id="imgModal">
                   <div class="modal-dialog modal-dialog-centered">
                       <div class="modal-content">
                           <div class="modal-header">
                               <h5 class="modal-title">Change Profile Image</h5>
                               <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                           </div>
                           <div class="modal-body">
                               <form method="post" name="form" enctype="multipart/form-data">
                                   <input type="hidden" name="admin_id" value="%s">
                                   <div class="mb-3">
                                       <label for="profileImage" class="form-label">Select New Image</label>
                                       <input type="file" id="profileImage" name="eimg" class="form-control" required>
                                   </div>
                                   <div>
                                       <input type="submit" class="btn btn-dark" name="eisubmit" value="Update Image">
                                       <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                   </div>
                               </form>
                           </div>
                       </div>
                   </div>
               </div>


               <div class="modal fade" id="editModal">
                   <div class="modal-dialog modal-dialog-centered">
                       <div class="modal-content">
                           <div class="modal-header">
                               <h5 class="modal-title">Edit Profile</h5>
                               <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                           </div>
                           <div class="modal-body">
                               <form method="post" name="form" enctype="multipart/form-data">
                                   <input type="hidden" name="edid" value="%s">
                                   <div class="mb-3">
                                       <label for="fullName" class="form-label">Full Name</label>
                                       <input type="text" id="fullName" name="ename" class="form-control" value="%s" required>
                                   </div>
                                   <div class="mb-3">
                                       <label for="location" class="form-label">Location</label>
                                       <input type="text" id="location" name="epass" class="form-control" value="%s" required>
                                   </div>
                                   <div class="text-center">
                                       <button type="submit" class="btn btn-dark" name="esubmit">Save Changes</button>
                                       <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                   </div>
                               </form>
                           </div>
                       </div>
                   </div>
               </div>


               <div class="modal fade" id="changeModal">
                   <div class="modal-dialog modal-dialog-centered">
                       <div class="modal-content">
                           <div class="modal-header">
                               <h5 class="modal-title">Change Password</h5>
                               <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                           </div>
                           <div class="modal-body">
                               <form method="post" name="form" enctype="multipart/form-data">
                                   <input type="hidden" name="chid" value="%s">
                                   <div class="mb-3 password-container">
                                       <label class="form-label">Current Password</label>
                                       <input type="password" id="currentPassword" name="currentpass" class="form-control" required>
                                       <i class="password-toggle fas fa-eye-slash" onclick="togglePasswordVisibility('currentPassword', this)"></i>
                                   </div>
                                   <div class="mb-3 password-container">
                                       <label class="form-label">New Password</label>
                                       <input type="password" id="newPassword" name="npass" class="form-control" required>
                                       <i class="password-toggle fas fa-eye-slash" onclick="togglePasswordVisibility('newPassword', this)"></i>
                                   </div>
                                   <div class="mb-3 password-container">
                                       <label class="form-label">Confirm Password</label>
                                       <input type="password" id="confirmPassword" name="cpass" class="form-control" required>
                                       <i class="password-toggle fas fa-eye-slash" onclick="togglePasswordVisibility('confirmPassword', this)"></i>
                                   </div>
                                   <div class="text-center">
                                       <input type="submit" class="btn btn-dark" name="psubmit" value="Update Password">
                                       <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                   </div>
                               </form>
                           </div>
                       </div>
                   </div>
               </div>
           </div>

           <script>
               document.getElementById("toggleSidebar").addEventListener("click", function() {
                   document.getElementById("sidebar").classList.toggle("active");
               });

               function togglePasswordVisibility(inputId, icon) {
                   const passwordInput = document.getElementById(inputId);

                   if (passwordInput.type === "password") {
                       passwordInput.type = "text";
                       icon.classList.remove("fa-eye-slash");
                       icon.classList.add("fa-eye");
                   } else {
                       passwordInput.type = "password";
                       icon.classList.remove("fa-eye");
                       icon.classList.add("fa-eye-slash");
                   }
               }
           </script>
       </body>
     </html>
 """ % (i[5], i[3], i[4], i[0], i[0], i[3], i[4], i[0]))

editname = form.getvalue("ename")
editloc = form.getvalue("epass")
editsubmit = form.getvalue("esubmit")
editid = form.getvalue("edid")
if editsubmit != None:
    q = """update admin set fullname='%s',location='%s' where Id="%s" """ % (editname, editloc, editid)
    cur.execute(q)
    con.commit()
    print("""
           <script>
           alert("Profile Updated Successfully")
           window.location.href="oprofile.py?id=%s"
           </script>
    """ % (editid))

currentpass = form.getvalue("currentpass")
newpass = form.getvalue("npass")
confirmpass = form.getvalue("cpass")
psubmit = form.getvalue("psubmit")
chid = form.getvalue("chid")

if psubmit:

    ch = "SELECT password FROM admin WHERE Id=%s"
    cur.execute(ch, (chid,))
    result = cur.fetchone()

    if result:
        stored_password = result[0]

        if currentpass != stored_password:
            print("""
                <script>
                    alert("Current password is incorrect.");
                    history.back();
                </script>
            """)

        elif newpass == currentpass:
            print("""
                <script>
                    alert("New password cannot be the same as the current password. Please enter a different password.");
                    window.location.href="oprofile.py?id=%s"
                </script>
            """)

        elif newpass != confirmpass:
            print("""
                <script>
                    alert("Confirm Password does not match New Password. Please try again.");
                    window.location.href="oprofile.py?id=%s"
                </script>
            """)

        else:

            update_query = "UPDATE admin SET password=%s WHERE Id=%s"
            cur.execute(update_query, (newpass, chid))
            con.commit()

            print("""
                <script>
                    alert("Password updated successfully.");
                    window.location.href="oprofile.py?id=%s";
                </script>
            """ % chid)

    else:
        print("""
            <script>
                alert("User not found.");
                window.location.href="oprofile.py?id=%s"
            </script>
        """)

isubmit = form.getvalue("eisubmit")

if isubmit != None:
    eimage = form['eimg']
    fn = os.path.basename(eimage.filename)
    open("images/" + fn, "wb").write(eimage.file.read())

    x = """update admin set image='%s' where Id='%s' """ % (fn, id)
    cur.execute(x)
    con.commit()

    print("""
            <script>
            alert("Profile Picture Updated Successfully");
            window.location.href="oprofile.py?id=%s";
            </script>
        """ % (id))