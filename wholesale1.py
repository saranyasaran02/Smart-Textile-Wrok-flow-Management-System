#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
product_filter = form.getvalue("product")
material_filter = form.getvalue("material")
size_filter = form.getvalue("size")


l = """select * from wholesaler where id='%s' """ % (uid)
cur.execute(l)
wholesaler_info = cur.fetchall()
wholesaler_name = wholesaler_info[0][1] if wholesaler_info else "Wholesaler"


query = "SELECT product_id, product, material, size, color, quantity, price, image FROM dispatch WHERE 1=1"
params = []

if product_filter:
    query += " AND product LIKE %s"
    params.append(f"%{product_filter}%")

if material_filter:
    query += " AND material = %s"
    params.append(material_filter)

if size_filter:
    query += " AND size = %s"
    params.append(size_filter)

cur.execute(query, params)
products = cur.fetchall()

print("Content-type:text/html\r\n\r\n")

# HTML Display
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wholesaler Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <style>
        :root {{
            --primary-color: #eddacf;
            --text-color: rgb(85, 77, 77);
            --hover-color: rgba(0, 0, 0, 0.1);
            --border-color: #ddd;
            --shadow-color: rgba(0, 0, 0, 0.1);
        }}

        body {{
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            overflow-x: hidden; 
        }}

        .sidebar {{
            background-color: var(--primary-color);
            height: 100vh;
            position: fixed;
            width: 250px;
            transition: all 0.3s ease;
            padding-top: 20px;
            left: 0;
            z-index: 1000;
            box-shadow: 2px 0 10px var(--shadow-color);
        }}

        .sidebar h4 {{
            color: var(--text-color);
            text-align: center;
            margin-bottom: 30px;
            font-weight: 600;
            letter-spacing: 1px;
        }}

        .sidebar .menu-item {{
            padding: 15px 20px;
            color: var(--text-color);
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            border-left: 4px solid transparent;
            margin-bottom: 5px;
        }}

        .sidebar .menu-item i {{
            margin-right: 15px;
            font-size: 18px;
            width: 20px;
            text-align: center;
        }}

        .sidebar .menu-item:hover {{
            font-weight: 600;
            background-color: var(--hover-color);
            transform: translateX(5px);
        }}

        .content {{
            padding: 30px;
            width: calc(100% - 250px); 
            margin-left: 250px;
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
            box-sizing: border-box; 
        }}

        .hamburger {{
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
        }}

        @media (max-width: 992px) {{
            .content {{
                margin-left: 0;
                padding: 30px 15px;
                width: 100%;
            }}
            .dealer-info {{
                margin-left: 0 !important;
                padding: 20px !important;
            }}
            .profile-card {{
                width: 100% !important;
                max-width: 500px;
            }}
            .sidebar {{
                left: -250px;
            }}
            .hamburger {{
                display: block;
            }}
            .sidebar.active {{
                left: 0;
            }}
        }}

        @media (max-width: 768px) {{
            .sidebar {{
                left: -250px;
                width: 250px;
            }}
            .content {{
                margin-left: 0;
                padding: 30px 15px;
                padding-top: 80px;
                width: 100%;
            }}
            .hamburger {{
                display: block;
            }}
            .sidebar.active {{
                left: 0;
            }}
            .page-title {{
                margin-left: 0 !important;
            }}
            .dealer-info {{
                padding: 15px !important;
            }}
            .info-row {{
                flex-direction: column;
                align-items: flex-start !important;
            }}
            .info-row .label {{
                margin-bottom: 5px;
            }}
        }}

        @media (min-width: 576px) {{
            .modal-dialog {{
                max-width: 500px;
            }}
        }}

        .product-container {{
            margin-top: 20px;
        }}

        .welcome-header {{
            margin-bottom: 20px;
        }}
    </style>
    <script>
        function openModal(productId, name, material, size, color, price) {{
            document.getElementById('productId').value = productId;
            document.getElementById('productName').value = name;
            document.getElementById('productMaterial').value = material;
            document.getElementById('productSize').value = size;
            document.getElementById('productColor').value = color;
            document.getElementById('productPrice').value = price;
            document.getElementById('quantity').value = 1;
            document.getElementById('totalPrice').innerText = price;

            const modalInstance = new bootstrap.Modal(document.getElementById('orderModal'));
            modalInstance.show();
        }}

        function updateTotalPrice() {{
            const price = parseFloat(document.getElementById('productPrice').value);
            const quantity = parseInt(document.getElementById('quantity').value);
            document.getElementById('totalPrice').innerText = price * quantity;
        }}
    </script>
</head>
<body>
    <div class="hamburger" >
        <i class="fa fa-bars"></i>
    </div>

    <div class="sidebar">
        <h4 style="margin-top:50px">Wholesaler Dashboard</h4><br>

        <div class="menu-item">
            <a href="wprofile.py?id={uid}" style="text-decoration: none;color:var(--text-color);">
                <i class="fa-solid fa-user"></i> Profile
            </a>
        </div>
        <div class="menu-item">
            <a href="whole_sale.py?id={uid}" style="text-decoration: none;color:var(--text-color);">
                <i class="fa-solid fa-shopping-cart"></i> Purchase Product
            </a>
        </div>
        <div class="menu-item">
            <a href="wholesale_view.py?id={uid}" style="text-decoration: none;color:var(--text-color);">
                <i class="fa-solid fa-eye"></i> Purchased Product
            </a>
        </div>
    </div>

    <div class="content" id="content">
        <div class="welcome-header">
            <h2>Welcome {wholesaler_name}</h2>
        </div>

        <div class="product-container">
            <h3>Available Products</h3>

           
            <form method="get" class="mb-4">
                <input type="hidden" name="id" value="{uid}">
                <div class="row">
                    <div class="col-md-3">
                        <input type="text" name="product" class="form-control" placeholder="Search Product" value="{product_filter or ''}">
                    </div>
                    <div class="col-md-3">
                        <select name="material" class="form-control">
                            <option value="">Select Material</option>
                            <option value="Rayon" {'selected' if material_filter == 'Rayon' else ''}>Rayon</option>
                            <option value="Popcorn" {'selected' if material_filter == 'Popcorn' else ''}>Popcorn</option>
                            <option value="Cotton" {'selected' if material_filter == 'Cotton' else ''}>Cotton</option>
                            <option value="Lycra" {'selected' if material_filter == 'Lycra' else ''}>Lycra</option>
                        </select>
                    </div>
                    <div class="col-md-3">
                        <select name="size" class="form-control">
                            <option value="">Select Size</option>
                            <option value="Small" {'selected' if size_filter == 'Small' else ''}>Small</option>
                            <option value="Medium" {'selected' if size_filter == 'Medium' else ''}>Medium</option>
                            <option value="Large" {'selected' if size_filter == 'Large' else ''}>Large</option>
                        </select>
                    </div>
                    <div class="col-md-3">
                        <button type="submit" class="btn btn-primary">Filter</button>
                    </div>
                </div>
            </form>

            <div class="row">
""")


for product in products:
    image_src = product[7] if product[7] else 'default.jpg'
    print(f"""
                <div class='col-md-4 mb-4'>
                    <div class='card'>
                        <img src='images/{image_src}' class='card-img-top' alt='Product Image' style='height: 200px; object-fit: cover;'>
                        <div class='card-body'>
                            <h5 class='card-title'>{product[1]} ({product[2]})</h5>
                            <p>Size: {product[3]} | Color: {product[4]}</p>
                            <p>Quantity: {product[5]} | Price: ${product[6]}</p>
                            <button class='btn btn-success' onclick="openModal('{product[0]}', '{product[1]}', '{product[2]}', '{product[3]}', '{product[4]}', '{product[6]}')">Order Now</button>
                        </div>
                    </div>
                </div>
    """)

print(f"""
            </div>
        </div>
    </div>

    
    <div class="modal fade" id="orderModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Place Your Order</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="place_order.py" method="post">
                        <input type="hidden" name="id" value="{uid}">
                        <input type="hidden" name="product_id" id="productId">
                        <div class="mb-3">
                            <label class="form-label">Product Name</label>
                            <input type="text" class="form-control" name="product_name" id="productName" readonly>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Material</label>
                            <input type="text" class="form-control" name="material" id="productMaterial" readonly>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Color</label>
                            <input type="text" class="form-control" name="color" id="productColor" readonly>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Size</label>
                            <input type="text" class="form-control" name="size" id="productSize" readonly>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Price</label>
                            <input type="text" class="form-control" name="price" id="productPrice" readonly>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Quantity</label>
                            <input type="number" class="form-control" name="quantity" id="quantity" min="1" required onchange="updateTotalPrice()">
                        </div>
                        <div class="mb-3">
                            <p class="form-text">Total Price: Rs <span id="totalPrice">0</span></p>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Place Order</button>
                    </form>
                </div>
            </div>
        </div>
    </div>



</body>
</html>
""")

con.close()