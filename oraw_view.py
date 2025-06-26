#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()
form = cgi.FieldStorage()
id = form.getvalue("dealer_id")

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
            margin-left: 350px;
            padding: 40px;
            max-width: 800px;
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


        .order-header {
            background-color: var(--primary-color);
            padding: 20px;
            border-radius: 12px 12px 0 0;
            margin-bottom: 0;
        }

        .order-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
        }

        .order-title i {
            margin-right: 12px;
            font-size: 1.8rem;
        }

        .order-body {
            background-color: white;
            border-radius: 0 0 12px 12px;
            padding: 25px;
            box-shadow: 0 6px 18px var(--shadow-color);
            margin-bottom: 30px;
        }

        .order-item {
            display: flex;
            justify-content: space-between;
            padding: 15px 0;
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }

        .order-item:last-child {
            border-bottom: none;
        }

        .order-item-name {
            font-weight: 600;
            color: var(--text-color);
            display: flex;
            align-items: center;
        }

        .order-item-name i {
            margin-right: 10px;
            color: var(--accent-color);
        }

        .order-item-value {
            font-weight: 500;
            color: #666;
        }

        .order-total {
            margin-top: 20px;
            padding-top: 20px;
            border-top: 2px dashed rgba(0,0,0,0.1);
        }

        .order-total-row {
            display: flex;
            justify-content: space-between;
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-color);
        }

        .order-material-badge {
            display: inline-block;
            background-color: var(--accent-color);
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            margin: 5px 0;
        }
    </style>
</head>
""")

x = """select * from admin"""
cur.execute(x)
res = cur.fetchall()
for i in res:
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
                    <a href="order_raw.py?id=%s"><i class="fas fa-box"></i> Dealer</a>
                </div>
                <div class="menu-item">
                    <a href="amanager.py?id="%s"><i class="fas fa-user-tie"></i> Manager</a>
                </div>
                <div class="menu-item">
                    <a href="adminwhole.py?id=%s"><i class="fas fa-box"></i> Wholesaler</a>
                </div>
            </div>""" % (i[0], i[0], i[0], i[0]))

l = """select * from raw where rid="%s" """ % (id)
cur.execute(l)
res = cur.fetchall()
for r in res:
    print("""
                <div class="content" id="content">

                    <div class="order-header">
                        <div class="order-title">
                            <i class="fas fa-box-open"></i> Order Details
                        </div>
                        <div class="order-material-badge">
                            %s
                        </div>
                    </div>

                    <div class="order-body">
                        <div class="order-item">
                            <div class="order-item-name">
                                <i class="fas fa-cube"></i>

                                %s - %s
                            </div>
                        </div>

                        <div class="order-item">
                            <div class="order-item-name">
                                <i class="fas fa-cube"></i> 

                                %s - %s
                            </div>
                        </div>

                        <div class="order-item">
                            <div class="order-item-name">
                                <i class="fas fa-cube"></i> 

                                %s - %s
                            </div>
                        </div>

                        <div class="order-total">
                            <div class="order-item">
                                <div class="order-item-name">
                                    <i class="fas fa-weight-hanging"></i> Total Quantity
                                </div>
                                <div class="order-item-value">
                                    %s
                                </div>
                            </div>

                            <div class="order-total-row">
                                <div>Total Price</div>
                                <div>%s</div>
                            </div>
                        </div>
                        <div class="mt-4 text-dark text-align text-center " style="font-weight:bold">
                          %s
                        </div>
                    </div>
                </div>
            """ % (r[13], r[14], r[17], r[15], r[18], r[16], r[19], r[20], r[21], r[22]))

print("""
        <script>
            document.getElementById('toggleSidebar').addEventListener('click', function() {
                document.getElementById('sidebar').classList.toggle('active');
            });
        </script>
    </body>
</html>
""")

con.close()