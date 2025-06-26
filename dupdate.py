#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os
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
            background-color: var(--card-bg);
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease;
            width: 90%;
            max-width: 700px;
            margin-top: 50px;
            border: none;
        }

        .profile-header {
            padding: 30px 0;
            text-align: center;
            position: relative;
            background-color: var(--primary-color);
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }

        .profile-header h4 {
            color: var(--text-color);
            font-weight: 700;
            margin: 0;
            padding-bottom: 8px;
            position: relative;
            display: inline-block;
        }

        .profile-header h4:after {
            content: '';
            position: absolute;
            width: 60px;
            height: 3px;
            background-color: var(--accent-color);
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 5px;
        }

        .profile-header p {
            color: var(--text-color);
            opacity: 0.8;
            margin-top: 8px;
        }

        .dealer-info {
            padding: 30px 40px;
            width: 100%;
            box-sizing: border-box;
            background-color: var(--form-bg);
        }

        .info-row {
            display: flex;
            padding: 16px 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            align-items: center;
            flex-wrap: wrap;
        }

        .info-row:last-child {
            border-bottom: none;
        }

        .info-row .label {
            font-weight: 600;
            color: var(--text-color);
            width: 130px;
            text-align: left;
            flex-shrink: 0;
            display: flex;
            align-items: center;
        }

        .info-row .label i {
            margin-right: 10px;
            width: 20px;
            text-align: center;
            color: var rgb(85, 77, 77);
            font-size: 18px;
        }

        .info-row .value {
            color: #555;
            text-align: left;
            flex-grow: 1;
            font-size: 16px;
            word-break: break-word;
            max-width: 100%;
        }

        .form-control {
            border-radius: 8px;
            padding: 12px 15px;
            border: 1px solid rgba(0, 0, 0, 0.1);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }

        .form-control:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 0 3px rgba(212, 168, 142, 0.2);
        }

        select.form-control {
            cursor: pointer;
            background-image: linear-gradient(45deg, transparent 50%, var(--text-color) 50%), linear-gradient(135deg, var(--text-color) 50%, transparent 50%);
            background-position: calc(100% - 20px) calc(50%), calc(100% - 15px) calc(50%);
            background-size: 5px 5px, 5px 5px;
            background-repeat: no-repeat;
            appearance: none;
        }

        .color-checkboxes {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 10px;
        }

        .color-checkbox {
            display: flex;
            align-items: center;
            margin-right: 10px;
        }

        .form-check-input {
            width: 18px;
            height: 18px;
            margin-right: 6px;
            cursor: pointer;
        }

        .form-check-input:checked {
            background-color: var(--accent-color);
            border-color: var(--accent-color);
        }

        .form-check-label {
            cursor: pointer;
            user-select: none;
        }

        .action-buttons {
            padding: 25px 0 10px;
            display: flex;
            justify-content: center;
        }

        .edit-btn {
            background-color: rgb(85, 77, 77);
            color: white;
            border: none;
            padding: 13px 35px;
            border-radius: 30px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(212, 168, 142, 0.3);
            letter-spacing: 0.5px;
            text-transform: uppercase;
            font-size: 14px;
        }

        .edit-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 18px rgba(212, 168, 142, 0.4);
            background-color:#eddacf ;
            color: rgb(85, 77, 77);
        }

        .edit-btn i {
            margin-right: 8px;
        }

        .file-upload {
            position: relative;
            display: inline-block;
            width: 100%;
        }

        .file-upload input[type="file"] {
            opacity: 0;
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            width: 100%;
            cursor: pointer;
        }

        .upload-field {
            display: flex;
            align-items: center;
            background-color: white;
            border: 1px dashed rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            padding: 12px 15px;
            color: #555;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .upload-field:hover {
            border-color: var(--accent-color);
            background-color: rgba(212, 168, 142, 0.05);
        }

        .upload-field i {
            margin-right: 10px;
            font-size: 20px;
            color: var(--accent-color);
        }

        .section-title {
            font-weight: 600;
            color: var(--text-color);
            margin: 15px 0 10px;
            font-size: 18px;
            border-left: 3px solid var(--accent-color);
            padding-left: 10px;
        }
    </style>
</head>
</html>
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
                       <a href="dealer_order_view.py?id=%s" style="text-decoration: none;color:var(--text-color);">
                           <i class="fa-solid fa-shopping-cart"></i> View Orders
                       </a>
                   </div>
               </div>

               <div class="content" id="content">
                     
                     <div class="content" id="content">
                           
                            
                            <div class="profile-card">
                                <div class="profile-header">
                                    <h4>Add Available Raw Materials</h4>
                                </div>
                                
                                <div class="dealer-info">
                                    <form method="post" enctype="multipart/form-data">
                                       
                                        
                                        <div class="info-row">
                                            <div class="label">
                                                <i class="fa-solid fa-shirt"></i> Material Type
                                            </div>
                                            <div class="value">
                                                <select name="mat" class="form-control" required>
                                                    <option value="">Select Material Type</option>
                                                    <option value="Cotton">Cotton</option>
                                                    
                                                    <option value="Rayon">Rayon</option>
                                                    <option value="lycra">Lycra</option>
                                                    <option value="Popcorn">Popcorn</option>
                                                </select>
                                            </div>
                                        </div>
                                        
                                        <div class="info-row">
                                            <div class="label">
                                                <i class="fa-solid fa-ruler"></i> Quantity
                                            </div>
                                            <div class="value">
                                                <input type="number" name="quan" class="form-control" placeholder="Quantity in meters" required>
                                            </div>
                                        </div>
                                         <div class="info-row">
                                            <div class="label">
                                                <i class="fa-solid fa-tag"></i> Price
                                            </div>
                                            <div class="value">
                                                <input type="number" name="price" class="form-control" step="0.01" placeholder="Price per meter" required>
                                            </div>
                                        </div>
                                        
                                        <div class="info-row">
                                            <div class="label">
                                                <i class="fa-solid fa-image"></i> Image
                                            </div>
                                            <div class="value">
                                                <input type="file" name="image" class="form-control" step="0.01"  required>
                                            </div>
                                        </div>
                                        
                                        
                                        <div class="info-row">
                                            <div class="label">
                                                <i class="fa-solid fa-palette"></i> Color
                                            </div>
                                            <div class="row mt-2">
                                                        <div class="col-sm-2 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="Black" name="color" value="Black">
                                                                <label class="form-check-label" for="Black"> Black</label>
                                                            </div>
                                                        </div>
                                                        <div class="col-sm-2 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="White" name="color" value="White">
                                                                <label class="form-check-label" for="White"> White</label>
                                                            </div>
                                                        </div>
                                                        
                                                        <div class="col-sm-2 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="Blue" name="color" value="Blue">
                                                                <label class="form-check-label" for="Blue"> Blue</label>
                                                            </div>
                                                        </div>
                                                         <div class="col-sm-2 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="Red" name="color" value="Red">
                                                                <label class="form-check-label" for="Red"> Red</label>
                                                            </div>
                                                        </div>
                                                        <div class="col-sm-2 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="Purple" name="color" value="Purple">
                                                                <label class="form-check-label" for="Purple">Purple </label>
                                                            </div>
                                                        </div>
                                                       
                                                        
                                                    </div>
                                        </div>
                                         
                                        
                                        
                                        
                                        
                                        <div class="action-buttons">
                                            <input type="submit" class="edit-btn" value="Add Material" name="update_submit">
                                                
                                            
                                        </div>
                                    </form>
                                </div>
                            </div>
                        
                            
                            
                        
                                <script>
                                    document.getElementById('toggleSidebar').addEventListener('click', function() {
                                        document.getElementById('sidebar').classList.toggle('active');
                                    });
                                    
                                  
                                    
                                </script>
                    </div> 
               </div>
         </body>
 </html>
                                           
                        """%(uid,uid,uid,uid))



umaterial=form.getvalue("mat")
uquantity=form.getvalue("quan")
uprice=form.getvalue("price")
ucolor=form.getvalue("color")

usubmit=form.getvalue("update_submit")

if usubmit != None:
        Image = form['image']
        fn = os.path.basename(Image.filename)
        open("images/" + fn, "wb").write(Image.file.read())

        u = """insert into raw(rid,material,quantity,price,color,image) values('%s','%s','%s','%s','%s','%s')""" %(uid,umaterial,uquantity,uprice,','.join(ucolor),fn)
        cur.execute(u)
        con.commit()
        print("""
        <script>
        alert("Product Updated Sucessfully")
         window.location.href="dupdate.py?id=%s";
        </script>
        """ % uid)


