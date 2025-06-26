#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os
import sys
import pymysql
import cgi
import cgitb

cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

print("Content-type: text/html\r\n\r\n")


form = cgi.FieldStorage()
user_id = form.getvalue("id")
product_id = form.getvalue("product_id")
order_id = form.getvalue("order_id")
payment_type = form.getvalue("payment_type")


card_number = form.getvalue("card_number")
card_holder = form.getvalue("card_holder")
expiry_date = form.getvalue("expiry_date")
cvv = form.getvalue("cvv")
upi_id = form.getvalue("upi_id")
bank_name = form.getvalue("bank_name")
wallet_type = form.getvalue("wallet_type")


try:
    con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
    cur = con.cursor()


    if payment_type and (
            (payment_type in ["Credit Card", "Debit Card"] and card_number and card_holder and expiry_date and cvv) or
            (payment_type == "UPI" and upi_id) or
            (payment_type == "NetBanking" and bank_name) or
            (payment_type == "Wallet" and wallet_type)):


        update_query = """UPDATE w_order 
                          SET payment_status='Paid', payment_method=%s
                          WHERE wholesaler_id=%s AND product_id=%s"""

        cur.execute(update_query, (payment_type, user_id, product_id))
        con.commit()


        if cur.rowcount > 0:

            print("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Payment Successful</title>
                <meta http-equiv="refresh" content="3;url=wholesale_view.py?id=%s">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f8f9fa;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .success-container {
                        background-color: white;
                        border-radius: 8px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                        padding: 20px;
                        text-align: center;
                        max-width: 400px;
                    }
                    .success-icon {
                        color: #4CAF50;
                        margin-bottom: 10px;
                    }
                    h1 {
                        color: #333;
                        margin-bottom: 10px;
                    }
                    p {
                        color: #666;
                        margin-bottom: 20px;
                    }
                    .btn {
                        background-color: #eddacf;
                        color: rgb(85, 77, 77);
                        border: none;
                        padding: 8px 15px;
                        border-radius: 4px;
                        text-decoration: none;
                        font-weight: bold;
                    }
                </style>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            </head>
            <body>
                <div class="success-container">
                    <div class="success-icon">
                        <i class="fas fa-check-circle fa-3x"></i>
                    </div>
                    <h1>Payment Successful!</h1>
                    <p>Your payment via <strong>%s</strong> has been processed successfully.</p>
                    <a href="wholesale_view.py?id=%s" class="btn">Back to Dashboard</a>
                </div>
            </body>
            </html>
            """ % (user_id, payment_type, user_id))
        else:
            # Error message
            print("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Payment Error</title>
                <meta http-equiv="refresh" content="5;url=wholesale_view.py?id=%s">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f8f9fa;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-container {
                        background-color: white;
                        border-radius: 8px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                        padding: 20px;
                        text-align: center;
                        max-width: 400px;
                    }
                    .error-icon {
                        color: #f44336;
                        margin-bottom: 10px;
                    }
                    h1 {
                        color: #333;
                        margin-bottom: 10px;
                    }
                    p {
                        color: #666;
                        margin-bottom: 20px;
                    }
                    .btn {
                        background-color: #eddacf;
                        color: rgb(85, 77, 77);
                        border: none;
                        padding: 8px 15px;
                        border-radius: 4px;
                        text-decoration: none;
                        font-weight: bold;
                    }
                </style>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            </head>
            <body>
                <div class="error-container">
                    <div class="error-icon">
                        <i class="fas fa-times-circle fa-3x"></i>
                    </div>
                    <h1>Payment Error</h1>
                    <p>There was an error processing your payment. Please try again.</p>
                    <a href="wholesale_view.py?id=%s" class="btn">Back to Dashboard</a>
                </div>
            </body>
            </html>
            """ % (user_id, user_id))
    else:
        # If no payment type selected yet, show payment selection form
        # Fetch product info for display
        product_query = """SELECT product_name, total_price FROM w_order
                          WHERE wholesaler_id=%s AND product_id=%s"""
        cur.execute(product_query, (user_id, product_id))
        product_info = cur.fetchone()

        if product_info:
            product_name = product_info[0]
            total_price = product_info[1]

            # Show payment selection form with payment details
            print("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Payment Details</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f8f9fa;
                        margin: 0;
                        padding: 20px;
                    }
                    .payment-container {
                        background-color: white;
                        border-radius: 8px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                        padding: 20px;
                        max-width: 500px;
                        margin: 0 auto;
                    }
                    h1 {
                        color: #333;
                        margin-bottom: 15px;
                        font-size: 22px;
                    }
                    .product-details {
                        background-color: #f5f5f5;
                        padding: 10px;
                        border-radius: 4px;
                        margin-bottom: 15px;
                    }
                    .product-name {
                        font-weight: bold;
                        margin-bottom: 5px;
                    }
                    .product-price {
                        color: #e74c3c;
                        font-weight: bold;
                    }
                    .payment-method {
                        margin-bottom: 10px;
                    }
                    .payment-details {
                        margin-top: 15px;
                        display: none;
                    }
                    input[type="text"], input[type="number"], select {
                        width: 100%;
                        padding: 8px;
                        margin: 5px 0 10px 0;
                        border: 1px solid #ddd;
                        border-radius: 4px;
                        box-sizing: border-box;
                    }
                    .button-group {
                        margin-top: 15px;
                    }
                    .btn {
                        background-color: #eddacf;
                        color: rgb(85, 77, 77);
                        border: none;
                        padding: 8px 15px;
                        border-radius: 4px;
                        text-decoration: none;
                        font-weight: bold;
                        cursor: pointer;
                        margin-right: 5px;
                    }
                    .btn-primary {
                        background-color: #6c5ce7;
                        color: white;
                    }
                </style>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            </head>""")
            print("""
            <body>
                <div class="payment-container">
                    <h1>Payment Details</h1>

                    <div class="product-details">
                        <div class="product-name">%s</div>
                        <div class="product-price">Rs %s</div>
                    </div>

                    <form action="process_payment.py" method="get">
                        <input type="hidden" name="id" value="%s">
                        <input type="hidden" name="product_id" value="%s">
                        <input type="hidden" name="order_id" value="%s">

                        <div class="payment-method">
                            <label>
                                <input type="radio" name="payment_type" value="Credit Card" onclick="showPaymentDetails('credit-card')" required> Credit Card
                            </label>
                        </div>

                        <div class="payment-method">
                            <label>
                                <input type="radio" name="payment_type" value="Debit Card" onclick="showPaymentDetails('debit-card')"> Debit Card
                            </label>
                        </div>

                        <div class="payment-method">
                            <label>
                                <input type="radio" name="payment_type" value="UPI" onclick="showPaymentDetails('upi')"> UPI Payment
                            </label>
                        </div>

                        <div class="payment-method">
                            <label>
                                <input type="radio" name="payment_type" value="NetBanking" onclick="showPaymentDetails('netbanking')"> Net Banking
                            </label>
                        </div>

                        <div class="payment-method">
                            <label>
                                <input type="radio" name="payment_type" value="Wallet" onclick="showPaymentDetails('wallet')"> Wallet
                            </label>
                        </div>

                      
                        <div id="credit-card" class="payment-details">
                            <label>Card Number:</label>
                            <input type="text" name="card_number" placeholder="1234 5678 9012 3456" maxlength="19">

                            <label>Card Holder Name:</label>
                            <input type="text" name="card_holder" placeholder="Name on card">

                            <div style="display: flex; gap: 10px;">
                                <div style="flex: 1;">
                                    <label>Expiry Date:</label>
                                    <input type="text" name="expiry_date" placeholder="MM/YY" maxlength="5">
                                </div>
                                <div style="flex: 1;">
                                    <label>CVV:</label>
                                    <input type="number" name="cvv" placeholder="123" maxlength="3">
                                </div>
                            </div>
                        </div>

                       
                        <div id="debit-card" class="payment-details">
                            <label>Card Number:</label>
                            <input type="text" name="card_number" placeholder="1234 5678 9012 3456" maxlength="19">

                            <label>Card Holder Name:</label>
                            <input type="text" name="card_holder" placeholder="Name on card">

                            <div style="display: flex; gap: 10px;">
                                <div style="flex: 1;">
                                    <label>Expiry Date:</label>
                                    <input type="text" name="expiry_date" placeholder="MM/YY" maxlength="5">
                                </div>
                                <div style="flex: 1;">
                                    <label>CVV:</label>
                                    <input type="number" name="cvv" placeholder="123" maxlength="3">
                                </div>
                            </div>
                        </div>

                      
                        <div id="upi" class="payment-details">
                            <label>UPI ID:</label>
                            <input type="text" name="upi_id" placeholder="yourname@upi">
                        </div>

                        
                        <div id="netbanking" class="payment-details">
                            <label>Select Bank:</label>
                            <select name="bank_name">
                                <option value="">Select your bank</option>
                                <option value="SBI">State Bank of India</option>
                                <option value="HDFC">HDFC Bank</option>
                                <option value="ICICI">ICICI Bank</option>
                                <option value="Axis">Axis Bank</option>
                                <option value="Canara">Canara Bank</option>
                            </select>
                        </div>

                        <div id="wallet" class="payment-details">
                            <label>Select Wallet:</label>
                            <select name="wallet_type">
                                <option value="">Select your wallet</option>
                                <option value="Paytm">Paytm</option>
                                <option value="PhonePe">PhonePe</option>
                                <option value="Amazon Pay">Amazon Pay</option>
                                <option value="Google Pay">Google Pay</option>
                            </select>
                        </div>

                        <div class="button-group">
                            <button type="submit" class="btn btn-dark">Pay Now</button>
                            <a href="wholesale_view.py?id=%s" class="btn">Cancel</a>
                        </div>
                    </form>
                </div>

                <script>
                    function showPaymentDetails(type) {
                      
                        document.querySelectorAll('.payment-details').forEach(div => {
                            div.style.display = 'none';
                        });

                        
                        document.getElementById(type).style.display = 'block';
                    }
                </script>
            </body>
            </html>
            """ % (product_name, total_price, user_id, product_id, order_id, user_id))
        else:
            # No product found
            print("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Product Not Found</title>
                <meta http-equiv="refresh" content="3;url=wholesale_view.py?id=%s">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f8f9fa;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .error-container {
                        background-color: white;
                        border-radius: 8px;
                        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                        padding: 20px;
                        text-align: center;
                        max-width: 400px;
                    }
                    .error-icon {
                        color: #f44336;
                        margin-bottom: 10px;
                    }
                    h1 {
                        color: #333;
                        margin-bottom: 10px;
                    }
                    p {
                        color: #666;
                        margin-bottom: 20px;
                    }
                    .btn {
                        background-color: #eddacf;
                        color: rgb(85, 77, 77);
                        border: none;
                        padding: 8px 15px;
                        border-radius: 4px;
                        text-decoration: none;
                        font-weight: bold;
                    }
                </style>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            </head>
            <body>
                <div class="error-container">
                    <div class="error-icon">
                        <i class="fas fa-exclamation-circle fa-3x"></i>
                    </div>
                    <h1>Product Not Found</h1>
                    <p>The requested product could not be found.</p>
                    <a href="wholesale_view.py?id=%s" class="btn">Back to Dashboard</a>
                </div>
            </body>
            </html>
            """ % (user_id, user_id))

except Exception as e:
    # Display any database errors
    print("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>System Error</title>
        <meta http-equiv="refresh" content="5;url=wholesale_view.py?id=%s">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f8f9fa;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .error-container {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                padding: 20px;
                text-align: center;
                max-width: 400px;
            }
            .error-icon {
                color: #f44336;
                margin-bottom: 10px;
            }
            h1 {
                color: #333;
                margin-bottom: 10px;
            }
            p {
                color: #666;
                margin-bottom: 20px;
            }
            .error-details {
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 4px;
                margin-bottom: 20px;
                text-align: left;
                overflow-x: auto;
            }
            .btn {
                background-color: #eddacf;
                color: rgb(85, 77, 77);
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body>
        <div class="error-container">
            <div class="error-icon">
                <i class="fas fa-exclamation-triangle fa-3x"></i>
            </div>
            <h1>System Error</h1>
            <p>There was an error while processing your payment:</p>
            <div class="error-details">%s</div>
            <a href="wholesale_view.py?id=%s" class="btn">Back to Dashboard</a>
        </div>
    </body>
    </html>
    """ % (user_id, str(e), user_id))
finally:
    # Close the database connection
    if 'con' in locals():
        con.close()