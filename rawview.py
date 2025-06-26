#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os

print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
x = """select * from raw where rid="%s" """ % (uid)
cur.execute(x)
res = cur.fetchall()
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
            --card-header: #55494e;
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
            padding: 40px;
            width: calc(100% - 250px); 
            position: relative;
            left: 250px;
            transition: all 0.3s ease;
            box-sizing: border-box;
            min-height: 100vh;
            background: linear-gradient(135deg, #f8f9fa 0%, #f1f1f1 100%);
        }

        .page-title {
            color: var(--text-color);
            font-weight: 700;
            margin-bottom: 50px;
            text-align: center;
            position: relative;
            padding-bottom: 15px;
        }

        .page-title:after {
            content: '';
            position: absolute;
            width: 100px;
            height: 3px;
            background-color: var(--accent-color);
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 30px;
            width: 100%;
        }

        .product-card {
            background-color: var(--card-bg);
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            height: 100%;
            max-height: 550px;
            position: relative;
        }

        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }

        .product-image-container {
            width: 100%;
            height: 280px;
            overflow: hidden;
            position: relative;
            background-color: #f9f9f9;
        }

        .product-image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.7s ease;
        }

        .product-card:hover .product-image-container img {
            transform: scale(1.08);
        }

        .product-status {
            position: absolute;
            top: 15px;
            right: 15px;
            background-color: rgba(76, 175, 80, 0.9);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            z-index: 10;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        }

        .product-header {
            padding: 18px 20px;
            background-color: var(--card-header);
            position: relative;
        }

        .product-header h4 {
            margin: 0;
            color: white;
            font-size: 18px;
            font-weight: 600;
            text-align: center;
            letter-spacing: 0.5px;
        }

        .product-details {
            padding: 25px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }

        .info-row {
            display: flex;
            padding: 12px 0;
            border-bottom: 1px solid var(--border-color);
            align-items: center;
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
            font-size: 14px;
        }

        .info-row .label i {
            margin-right: 12px;
            width: 16px;
            text-align: center;
            color: var(--accent-color);
        }

        .info-row .value {
            color: #555;
            text-align: left;
            flex-grow: 1;
            font-size: 15px;
            word-break: break-word;
            font-weight: 500;
        }

        .action-buttons {
            text-align: center;
            padding: 18px;
            background-color: #fcfcfc;
            border-top: 1px solid var(--border-color);
            margin-top: auto;
        }

        .btn-update {
            background-color: var(--card-header);
            border: none;
            border-radius: 30px;
            padding: 12px 30px;
            font-size: 14px;
            transition: all 0.3s ease;
            font-weight: 600;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            color: white;
        }

        .btn-update:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
            background-color: #463f42;
            color: white;
        }

        .btn-update i {
            margin-right: 8px;
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

        .stats-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }

        .stat-card {
            flex: 1;
            min-width: 200px;
            background-color: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            margin: 0 10px 20px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }

        .stat-icon {
            display: inline-block;
            width: 60px;
            height: 60px;
            line-height: 60px;
            text-align: center;
            background-color: rgba(212, 168, 142, 0.2);
            border-radius: 50%;
            margin-bottom: 15px;
            color: var(--accent-color);
            font-size: 24px;
        }

        .stat-value {
            font-size: 28px;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 5px;
        }

        .stat-label {
            color: #777;
            font-size: 14px;
        }

        @media (max-width: 1200px) {
            .product-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            .stats-container {
                flex-wrap: wrap;
            }
            .stat-card {
                min-width: calc(50% - 20px);
                margin-bottom: 20px;
            }
        }

        @media (max-width: 992px) {
            .content {
                width: 100%;
                left: 0;
                padding: 80px 30px 30px;
            }
            .product-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 768px) {
            .sidebar {
                left: -250px;
            }
            .sidebar.active {
                left: 0;
            }
            .hamburger {
                display: block;
            }
            .product-grid {
                grid-template-columns: 1fr;
            }
            .stat-card {
                min-width: 100%;
            }
        }

        .modal-content {
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }

        .modal-header {
            background-color: var(--card-header);
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
        """)
print("""

</head>
<body>
    <div class="hamburger" id="toggleSidebar">
        <i class="fa fa-bars"></i>
    </div>

    <div class="sidebar" id="sidebar">
        <h4 style="margin-top:50px">Dealer Dashboard</h4><br>
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
    </div>""" % (uid, uid, uid,uid))

print("""<div class="content">
        <h2 class="page-title">Product Inventory Dashboard</h2>

        <!-- Stats Container -->
        <div class="stats-container">
            <div class="stat-card">
                <div class="stat-icon">
                    <i class="fa-solid fa-box"></i>
                </div>
                <div class="stat-value">%d</div>
                <div class="stat-label">Total Products</div>
            </div>

            <div class="stat-card">
                <div class="stat-icon">
                    <i class="fa-solid fa-indian-rupee-sign"></i>
                </div>
                <div class="stat-value">Rs.%.2f</div>
                <div class="stat-label">Avg. Price</div>
            </div>

            
        </div>

        <div class="product-grid">""" % (len(res), sum([float(i[4]) for i in res]) / len(res) if res else 0))

for i in res:
    product_id = i[0]

    print("""
    <!-- Product card -->
    <div class="product-card" data-aos="fade-up" data-aos-delay="100">
        <div class="product-status">In Stock</div>
        <div class="product-image-container">
            <img src="./images/%s" alt="Product Image">
        </div>
        <div class="product-header">
            <h4>Product Details</h4>
        </div>
        <div class="product-details">
            <div class="info-row">
                <span class="label"><i class="fa-solid fa-shirt"></i> Material:</span>
                <span class="value">%s</span>
            </div>
            <div class="info-row">
                <span class="label"><i class="fa-solid fa-cubes"></i> Quantity:</span>
                <span class="value">%s units</span>
            </div>
            <div class="info-row">
                <span class="label"><i class="fa-solid fa-tag"></i> Price:</span>
                <span class="value">Rs.%s</span>
            </div>
            <div class="info-row">
                <span class="label"><i class="fa-solid fa-palette"></i> Color:</span>
                <span class="value">%s</span>
            </div>
        </div>
        <div class="action-buttons">
            <button type="button" class="btn btn-update" data-bs-toggle="modal" data-bs-target="#updateModal%s">
                <i class="fa-solid fa-pen-to-square"></i> Update Product
            </button>
        </div>
    </div>
    """ % (i[7], i[2], i[3], i[4], i[6], product_id))

print("""
        </div>
    </div>
""")

for i in res:
    product_id = i[0]
    print("""
    <!-- Modal for updating product -->
    <div class="modal fade" id="updateModal%s">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Update Product Information</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form method="post" action="rawview.py?id=%s" enctype="multipart/form-data">
                        <div class="mb-4">
                            <label for="quantity%s" class="form-label">Update Quantity</label>
                            <div class="input-group">
                                <span class="input-group-text"><i class="fa-solid fa-cubes"></i></span>
                                <input type="number" id="quantity%s" name="equan" class="form-control" placeholder="Enter quantity" required>
                            </div>
                        </div>

                        <div class="mb-4">
                            <label for="price%s" class="form-label">Update Price</label>
                            <div class="input-group">
                                <span class="input-group-text"><i class="fa-solid fa-dollar-sign"></i></span>
                                <input type="number" id="price%s" name="eprice" class="form-control" placeholder="Enter price" required>
                            </div>
                        </div>

                        <div class="mb-4">
                            <label class="form-label">Update Color</label>
                            <div class="color-option">
                                <div class="color-checkbox">
                                    <input class="color-input" type="checkbox" id="Black%s" name="ecolor" value="Black">
                                    <label for="Black%s">Black</label>
                                </div>
                                <div class="color-checkbox">
                                    <input class="color-input" type="checkbox" id="White%s" name="ecolor" value="White">
                                    <label for="White%s">White</label>
                                </div>
                                <div class="color-checkbox">
                                    <input class="color-input" type="checkbox" id="Blue%s" name="ecolor" value="Blue">
                                    <label for="Blue%s">Blue</label>
                                </div>
                                <div class="color-checkbox">
                                    <input class="color-input" type="checkbox" id="Red%s" name="ecolor" value="Red">
                                    <label for="Red%s">Red</label>
                                </div>
                                <div class="color-checkbox">
                                    <input class="color-input" type="checkbox" id="Purple%s" name="ecolor" value="Purple">
                                    <label for="Purple%s">Purple</label>
                                </div>
                            </div>
                        </div>

                        <div class="mb-4">
                            <label for="profileImage%s" class="form-label">Select New Image</label>
                            <div class="input-group">
                                <span class="input-group-text"><i class="fa-solid fa-image"></i></span>
                                <input type="file" id="profileImage%s" name="eimg" class="form-control" required>
                            </div>
                        </div>

                        <div class="d-flex justify-content-between mt-4">
                            <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">
                                <i class="fa-solid fa-times"></i> Cancel
                            </button>
                            <button type="submit" class="btn btn-update" name="esubmit">
                                <i class="fa-solid fa-check"></i> Update Product
                            </button>
                            <input type="hidden" value="%s" name="epid">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    """ % (product_id, uid,
           product_id, product_id,
           product_id, product_id,
           product_id, product_id,
           product_id, product_id,
           product_id, product_id,
           product_id, product_id,
           product_id, product_id,
           product_id, product_id,
           product_id))

print("""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
    <script>
        document.getElementById('toggleSidebar').addEventListener('click', function() {
            document.getElementById('sidebar').classList.toggle('active');
        });

        // Initialize AOS animation library
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true
        });
    </script>
""")

editquan = form.getvalue("equan")
editprice = form.getvalue("eprice")
editcolor = form.getvalue("ecolor")
editsubmit = form.getvalue("esubmit")
product_id = form.getvalue("epid")

if editsubmit is not None and product_id is not None:

    if 'eimg' in form:
        eimage = form['eimg']
        fn = os.path.basename(eimage.filename)
        open("images/" + fn, "wb").write(eimage.file.read())

        q = """UPDATE raw SET quantity='%s', price='%s', color='%s', image='%s' 
               WHERE dealerid='%s' AND rid='%s'""" % (editquan, editprice, ' '.join(editcolor), fn, product_id, uid)
        cur.execute(q)
        con.commit()

        print("""
        <script>
        alert("Product Updated Successfully")
        window.location.href="rawview.py?id=%s"
        </script>
        """ % (uid))

print("</body></html>")