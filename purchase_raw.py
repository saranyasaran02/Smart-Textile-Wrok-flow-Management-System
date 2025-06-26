#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("dealer_id")
x = """select * from admin  """
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
                         --card-bg: #ffffff;
                         --accent-color: #c9a99d;
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
                        padding: 40px;
                        max-width: 900px;
                        margin-right: auto;

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



                     .page-title {
                         color: var(--text-color);
                         font-weight: 700;
                         margin-bottom: 30px;
                         position: relative;
                         display: inline-block;
                     }

                     .page-title:after {
                         content: '';
                         position: absolute;
                         bottom: -10px;
                         left: 0;
                         width: 60px;
                         height: 3px;
                         background-color: var(--accent-color);
                     }

                     .material-card {
                         background-color: var(--card-bg);
                         border-radius: 12px;
                         box-shadow: 0 6px 18px var(--shadow-color);
                         padding: 25px;
                         margin-bottom: 30px;

                     }

                     .material-card:hover {
                         box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);

                     }

                     .material-header {
                         border-bottom: 1px solid rgba(0, 0, 0, 0.1);
                         padding-bottom: 15px;
                         margin-bottom: 20px;

                     }

                     .material-title {
                         font-size: 1.8rem;
                         font-weight: 600;
                         color: var(--text-color);
                         margin-bottom: 5px;
                     }

                     .material-subtitle {
                         color: var(--accent-color);
                         font-size: 1rem;
                         font-weight: 500;
                     }

                     .material-info {
                         display: flex;
                         align-items: center;
                         justify-content: space-between;
                         flex-wrap: wrap;
                     }

                     .material-details {
                         flex: 1;
                         min-width: 300px;
                     }

                     .material-image {
                         flex: 0 0 200px;
                         text-align: center;
                         padding: 15px;
                     }

                     .material-image img {
                         width: 150px;
                         height: 150px;
                         object-fit: cover;
                         border-radius: 8px;
                         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);

                     }



                     .info-row {
                         margin-bottom: 20px;
                         position: relative;
                         padding-left: 30px;
                     }

                     .info-row i {
                         position: absolute;
                         left: 0;
                         top: 3px;
                         color: var(--accent-color);
                         font-size: 1.2rem;
                     }

                     .info-label {
                         font-weight: 600;
                         color: var(--text-color);
                         margin-right: 10px;
                         font-size: 1.05rem;
                     }

                     .info-value {
                         color: #666;
                         font-weight: 500;
                     }
                     .material-footer {
                         margin-top: 20px;
                         padding-top: 15px;
                         border-top: 1px solid rgba(0, 0, 0, 0.1);
                         display: flex;
                         justify-content: flex-end;
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
                         .material-info {
                             flex-direction: column-reverse;
                         }
                         .material-image {
                             margin-bottom: 20px;
                         }
                     }
                     .btn-dark {
                         background-color:rgb(85, 77, 77);
                         border: none;
                         padding: 10px 20px;
                         font-weight: 600;
                         border-radius: 8px;

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
                         <a href="sale_product.py?id=%s"><i class="fas fa-box"></i> Wholesaler</a>
                   </div>
               </div>""" % (i[0], i[0], i[0],i[0]))

l = """select * from raw where rid="%s" """ % (id)
cur.execute(l)
result = cur.fetchall()

for x in result:
    print("""

           <div class="content" id="content">



               <div class="material-card">
                   <div class="material-header">
                       <h3 class="material-title">%s</h3>
                       <div class="material-subtitle">Raw Material Specification</div>
                   </div>

                   <div class="material-info">
                       <div class="material-details">
                           <div class="info-row">
                               <i class="fas fa-tag"></i>
                               <span class="info-label">Material:</span>
                               <span class="info-value">%s</span>
                           </div>

                           <div class="info-row">
                               <i class="fas fa-cubes"></i>
                               <span class="info-label">Quantity:</span>
                               <span class="info-value">%s units</span>
                           </div>

                           <div class="info-row">
                               <i class="fa-solid fa-indian-rupee-sign"></i>
                               <span class="info-label">Price Per Unit:</span>
                               <span class="info-value">Rs %s</span>
                           </div>

                           <div class="info-row">
                                <i class="fas fa-palette"></i>
                                <span class="info-label">Color:%s</span>

                            </div>


                       </div>

                       <div class="material-image">
                           <img src="./images/%s" >
                       </div>
                   </div>

                   <div class="material-footer">
                       <button class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#purchaseModal%s">
                           <i class="fa-solid fa-cart-shopping"></i> Purchase

                       </button>


                   </div>
               </div>
            </div>


               <!-- Modal for purchasing -->
                <div class="modal fade" id="purchaseModal%s" tabindex="-1" aria-labelledby="purchaseModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="purchaseModalLabel">Purchase Material: %s</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form id="purchaseForm%s" method="post">
                                    <input type="hidden" name="raw_id" value="%s">
                                    <input type="hidden" name="price_per_unit" value="%s">


                                    <div class="mb-4">
                                        <label class="form-label fw-bold">Select Colors and Quantities:</label>
                                    </div>


                                    <div class="mb-4">
                                        <div class="row mb-3">
                                            <div class="col-6">
                                                <div class="form-check">
                                                    <label class="form-check-label mb-4">Color :%s</label>
                                                    <input type="text" name="ecolor1"  placeholder="Enter the color"   class="form-control color-input" required><br>
                                                    <input type="text" name="ecolor2"  placeholder="Enter the color"  class="form-control color-input"><br>
                                                    <input type="text" name="ecolor3"  placeholder="Enter the color"  class="form-control color-input">
                                                </div>

                                            </div>
                                            <div class="col-6">
                                                <label class="form-check-label mb-4">Quantity :</label>
                                                <input type="number" class="form-control color-quantity mt-6" name="quantity_bwrone" min="0" value="%s" placeholder="Enter the quantity" ><br>
                                                <input type="number" class="form-control color-quantity mt-6" name="quantity_bwrtwo" min="0" value="%s" placeholder="Enter the quantity" ><br>
                                                <input type="number" class="form-control color-quantity mt-6" name="quantity_bwrthree" min="0" value="%s" placeholder="Enter the quantity" >
                                            </div>
                                        </div>




                                    </div>

                                    <div class="row mb-3">
                                        <div class="col-6">
                                            <label class="form-label fw-bold">Total Quantity:</label>
                                            <input type="text" class="form-control" id="totalQuantity%s" name="ototalq" readonly value="0"><br>
                                        </div>
                                        <div class="col-6">
                                            <label class="form-label fw-bold">Total Price (Rs):</label>
                                            <input type="text" class="form-control" id="totalPrice%s" name="ototalp" readonly value="0">
                                        </div>
                                    </div>
                                    <input type="hidden" name="omaterial" value="%s">

                                    <div class="d-grid">
                                        <input type="submit" class="btn btn-dark" value="Confirm Purchase" name="osubmit">



                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>""" % (
    x[2], x[2], x[3], x[4], x[6], x[7], x[0], x[0], x[2], x[0], x[0], x[4], x[6], x[6], x[6], x[6], x[0], x[0], x[2]))

    print("""     <script>
                     document.getElementById("toggleSidebar").addEventListener("click", function() {
                   document.getElementById("sidebar").classList.toggle("active");
               });

                    document.addEventListener('DOMContentLoaded', function() {
                        const modalId = 'purchaseModal%s';
                        const modal = document.getElementById(modalId);

                        if (modal) {
                            const formId = 'purchaseForm%s';
                            const form = document.getElementById(formId);
                            const pricePerUnit = %s; 
                            const quantityInputs = form.querySelectorAll('.color-quantity');


                            quantityInputs.forEach(function(input) {
                                input.addEventListener('input', updateTotals);
                            });


                            function updateTotals() {
                                let totalQuantity = 0;


                                quantityInputs.forEach(function(input) {
                                    totalQuantity += parseInt(input.value) || 0;
                                });


                                const totalPrice = totalQuantity * pricePerUnit;


                                document.getElementById('totalQuantity%s').value = totalQuantity;
                                document.getElementById('totalPrice%s').value = totalPrice.toFixed(2);
                            }


                            form.addEventListener('submit', function(event) {
                                const totalQuantity = parseInt(document.getElementById('totalQuantity%s').value);

                                if (totalQuantity <= 0) {
                                    event.preventDefault();
                                    alert('Please enter at least one quantity greater than 0.');
                                }
                            });
                        }
                    });




                </script>
         </body>
</html>
 (""" % (
        x[0], x[0], x[4],
        x[0], x[0], x[0]))

order_material = form.getvalue("omaterial")
order_color1 = form.getvalue("ecolor1")
order_color2 = form.getvalue("ecolor2")
order_color3 = form.getvalue("ecolor3")
order_quan1 = form.getvalue("quantity_bwrone")
order_quan2 = form.getvalue("quantity_bwrtwo")
order_quan3 = form.getvalue("quantity_bwrthree")
total_quan = form.getvalue("ototalq")
total_price = form.getvalue("ototalp")

order_submit = form.getvalue("osubmit")

if order_submit != None:
    w = """update raw set ordermat="%s",orderclrone="%s",orderclrtwo="%s",orderclrthree="%s",orderqone="%s",orderqtwo="%s",orderqthree="%s",orderqtotal="%s",orderptotal="%s" where rid="%s" and material="%s" """ % (
    order_material, order_color1, order_color2, order_color3, order_quan1, order_quan2, order_quan3, total_quan,
    total_price, id, order_material)
    cur.execute(w)
    con.commit()
    print("""

        <script>
        alert("Orderd  Sucessfully")
        </script>"""
          )

