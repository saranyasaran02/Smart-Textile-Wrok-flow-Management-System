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


                     .content {
                        margin-left: 300px;
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

                    
                     .modal {
                         z-index: 2000;!importent
                     }

                     .modal-backdrop {
                         z-index: 1500;!important
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


                     .manufacturing-container {
                         background-color: white;
                         border-radius: 15px;
                         box-shadow: 0 5px 15px var(--shadow-color);
                         padding: 25px;
                         margin-bottom: 25px;
                     }

                     .manufacturing-header {
                         color: var(--text-color);
                         border-bottom: 2px solid var(--primary-color);
                         padding-bottom: 15px;
                         margin-bottom: 20px;
                     }

                     .form-label {
                         color: var(--text-color);
                         font-weight: 600;
                     }

                     .btn-submit {
                         background-color: var(--primary-color);
                         color: var(--text-color);
                         border: none;
                         font-weight: 600;
                         padding: 12px 25px;
                         border-radius: 8px;
                         transition: all 0.3s;
                         box-shadow: 0 3px 10px var(--shadow-color);
                     }

                     .btn-submit:hover {
                         transform: translateY(-3px);
                         box-shadow: 0 5px 15px var(--shadow-color);
                     }

                     .product-list {
                         margin-top: 40px;
                     }

                     .product-card {
                         background-color: var(--primary-color);
                         border-radius: 10px;
                         padding: 20px;
                         margin-bottom: 20px;
                         box-shadow: 0 3px 10px var(--shadow-color);
                         transition: all 0.3s;
                     }

                     .product-card:hover {
                         transform: translateY(-5px);
                         box-shadow: 0 8px 20px var(--shadow-color);
                     }

                     .product-title {
                         color: var(--text-color);
                         font-weight: 600;
                         margin-bottom: 15px;
                         border-bottom: 1px solid rgba(85, 77, 77, 0.2);
                         padding-bottom: 10px;
                     }

                     .product-info {
                         display: flex;
                         flex-wrap: wrap;
                     }

                     .product-detail {
                         flex: 1 0 50%;
                         margin-bottom: 10px;
                     }

                     .product-label {
                         font-weight: 600;
                         color: var(--text-color);
                     }

                     .status-badge {
                         float: right;
                         padding: 5px 10px;
                         border-radius: 20px;
                         font-size: 0.8rem;
                         font-weight: 600;
                     }

                     .status-pending {
                         background-color: #ffeeba;
                         color: #856404;
                     }

                     .status-approved {
                         background-color: #d4edda;
                         color: #155724;
                     }

                     .status-rejected {
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

                         .product-detail {
                             flex: 1 0 100%;
                         }
                     }

                     
                     .modal-dispatch {
                         max-width: 500px;
                     }

                     .dispatch-form label {
                         font-weight: 600;
                         margin-top: 10px;
                     }

                     .btn-dispatch {
                         background-color: #28a745;
                         color: white;
                         border: none;
                         padding: 6px 12px;
                         border-radius: 4px;
                         transition: all 0.2s;
                     }

                     .btn-dispatch:hover {
                         background-color: #218838;
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

               </div>""" % (id, id, id, id))
    print("""
           <div class="content" id="content">
               <h2 class="mb-4">Manufacturing Requirements</h2>


               <div class="manufacturing-container" >
                   <h4 class="manufacturing-header">Add New Manufacturing Request</h4>
                   <form  method="post" enctype="multipart/form-data">


                       <div class="row mb-3">
                           <div class="col-md-6 mb-3">
                               <label for="productName" class="form-label">Product Name</label>
                               <input type="text" class="form-control" id="productName" name="product" required>
                           </div>
                           <div class="col-md-6 mb-3">
                               <label for="materialType" class="form-label">Material Type</label>
                               <select class="form-control" id="materialType" name="material" required>
                                   <option value="">Select Material</option>
                                   <option value="Cotton">Cotton</option>
                                   <option value="Lycra">Lycra</option>
                                   <option value="Rayon">Rayon</option>
                                   <option value="Popcorn">Popcorn</option>

                               </select>
                           </div>
                       </div>

                       <div class="row mb-3">
                           <div class="col-md-6 mb-3">
                               <label for="color" class="form-label">Color</label>
                               <input type="text" class="form-control" id="color" name="color" required>
                           </div>
                           <div class="col-md-6 mb-3">
                               <label for="quantity" class="form-label">Quantity</label>
                               <input type="number" class="form-control" id="quantity" name="quantity" min="1" required>
                           </div>
                       </div>

                       <div class="row mb-3">
                           <div class="col-md-6 mb-3">
                               <label for="size" class="form-label">Size</label>
                               <input type="text" class="form-control" id="size" name="size" placeholder="e.g., Small" required>
                           </div>
                           <div class="col-md-6 mb-3">
                               <label for="deadline" class="form-label">Required By (Deadline)</label>
                               <input type="date" class="form-control" id="deadline" name="deadline" required>
                           </div>
                       </div>

                       <div class="mb-3">
                           <label for="specifications" class="form-label">Additional Specifications</label>
                           <textarea class="form-control" id="specifications" name="specifications" rows="3" placeholder="Enter any additional details or specifications..."></textarea>
                       </div>
                       <div>
                               <label for="price" class="form-label">Price</label>
                               <input type="number" class="form-control" id="price" name="price" min="1" required>
                           </div>
                           <div>
                               <label for="image" class="form-label">image</label>
                               <input type="file" class="form-control" id="image" name="image"  required>
                           </div>



                       <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                           <input type="submit" class="btn btn-submit" value="Submit Manufacturing Request" name="mrequest">
                       </div>
                   </form>
               </div>
               <div>
               <form method="post">
               <input type="submit" class="btn btn-submit" value="View Finished Products" name="fproduct">
               </form>
               </div>
""")


confirm_dispatch = form.getvalue("confirm_dispatch")
if confirm_dispatch != None:
    product_id = form.getvalue("product_id")
    product_name = form.getvalue("product")
    material = form.getvalue("material")
    size = form.getvalue("size")
    color = form.getvalue("color")
    price = form.getvalue("price")
    image = form.getvalue("image")
    dispatch_quantity = form.getvalue("dispatch_quantity")
    dispatch_notes = form.getvalue("dispatch_notes") or ""


    dispatch_query = """INSERT INTO dispatch (product_id, product, material, size, color, quantity, price, image) 
                        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
        product_id, product_name, material, size, color, dispatch_quantity, price, image)

    try:
        cur.execute(dispatch_query)


        select_query = """SELECT quantity FROM production WHERE id='%s'""" % (product_id)
        cur.execute(select_query)
        current_quantity = cur.fetchone()[0]
        new_quantity = int(current_quantity) - int(dispatch_quantity)

        if new_quantity > 0:
            update_query = """UPDATE production SET quantity='%s' WHERE id='%s'""" % (new_quantity, product_id)
        else:

            update_query = """UPDATE production SET quantity='0' WHERE id='%s'""" % (product_id)

        cur.execute(update_query)
        con.commit()

        print("""
            <script>
            alert("Product dispatched successfully!");
            location.href="amanager.py?id=%s";
            </script>""" % (id)
              )
    except Exception as e:
        print("""
            <script>
            alert("Error dispatching product: %s");
            location.href="amanager.py?id=%s";
            </script>""" % (str(e).replace("'", "\\'"), id)
              )

mproduct = form.getvalue("product")
mmaterial = form.getvalue("material")
mquantity = form.getvalue("quantity")
msize = form.getvalue("size")
mcolor = form.getvalue("color")
minfo = form.getvalue("specifications")
msubmit = form.getvalue("mrequest")
mdate = form.getvalue("deadline")
mprice = form.getvalue("price")

if msubmit != None:

    if 'image' in form:
        wsimage = form['image']
        fn = os.path.basename(wsimage.filename)
        open("images/" + fn, "wb").write(wsimage.file.read())


        x = """insert into production (product,material,size,color,quantity,deadline,info,status,price,image) values('%s','%s','%s','%s','%s','%s','%s','Requested','%s','%s')""" % (
            mproduct, mmaterial, msize, mcolor, mquantity, mdate, minfo, mprice, fn)
        cur.execute(x)
        con.commit()
        print("""
               <script>
               alert("Production Details Sent successfully !")
               location.href="amanager.py?id=%s"
               </script>""" % (id)
              )
    else:
        print("""
               <script>
               alert("Error: Image file is required!")
               </script>"""
              )


finished = form.getvalue("fproduct")
if finished != None:
    d = """select * from production where status="finished" and quantity !="0" """
    cur.execute(d)
    res_finished = cur.fetchall()

    print("""
    <div class="manufacturing-container mt-4" data-aos="fade-up">
        <h4 class="manufacturing-header">Finished Products</h4>
        <div class="table-responsive">
            <table class="table table-hover">
                <thead class="table-light">
                    <tr>
                        <th>Product</th>
                        <th>Material</th>
                        <th>Size</th>
                        <th>Color</th>
                        <th>Quantity</th>
                        <th>Deadline</th>
                        <th>Status</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
    """)

    if len(res_finished) > 0:
        for product in res_finished:
            product_id = product[0]
            print(f"""
                <tr>
                    <td>{product[1]}</td>
                    <td>{product[2]}</td>
                    <td>{product[3]}</td>
                    <td>{product[4]}</td>
                    <td>{product[5]}</td>
                    <td>{product[6]}</td>
                    <td><span class="badge bg-success">{product[7]}</span></td>
                    <td>
                        <button type="button" class="btn btn-dispatch" 
                            data-bs-toggle="modal" 
                            data-bs-target="#dispatchModal{product_id}">
                            Dispatch
                        </button>

                        <!-- Dispatch Modal for product {product_id} -->
                        <div class="modal fade" id="dispatchModal{product_id}" tabindex="-1" aria-labelledby="dispatchModalLabel{product_id}" aria-hidden="true">
                            <div class="modal-dialog modal-dispatch">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="dispatchModalLabel{product_id}">Dispatch {product[1]}</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <form action="amanager.py?id={id}" method="post" class="dispatch-form">
                                            <input type="hidden" name="product_id" value="{product_id}">
                                            <input type="hidden" name="product" value="{product[1]}">
                                            <input type="hidden" name="material" value="{product[2]}">
                                            <input type="hidden" name="size" value="{product[3]}">
                                            <input type="hidden" name="color" value="{product[4]}">
                                            <input type="hidden" name="quantity" value="{product[5]}">
                                            <input type="hidden" name="price" value="{product[9]}">
                                            <input type="hidden" name="image" value="{product[10]}">

                                            <div class="mb-3">
                                                <label for="dispatchQuantity{product_id}" class="form-label">Quantity to Dispatch</label>
                                                <input type="number" class="form-control" id="dispatchQuantity{product_id}" name="dispatch_quantity" min="1" max="{product[5]}" required>
                                                <div class="form-text">Available quantity: {product[5]}</div>
                                            </div>

                                            
                                            <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                                                <button type="button" class="btn btn-secondary me-md-2" data-bs-dismiss="modal">Cancel</button>
                                                <input type="submit" class="btn btn-success" value="Confirm Dispatch" name="confirm_dispatch">
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            """)
    else:
        print("""
                <tr>
                    <td colspan="8" class="text-center">No finished products found.</td>
                </tr>
        """)

    print("""
                </tbody>
            </table>
        </div>
    </div>
    """)

print("""               
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

       
        document.addEventListener('DOMContentLoaded', function() {
        
            const modals = document.querySelectorAll('.modal');
            modals.forEach(modal => {
                modal.addEventListener('shown.bs.modal', function() {
                    console.log('Modal shown: ' + modal.id);
                });

                modal.addEventListener('hidden.bs.modal', function() {
                    console.log('Modal hidden: ' + modal.id);
                });
            });
        });
        </script>
       </body>
     </html>
 """)