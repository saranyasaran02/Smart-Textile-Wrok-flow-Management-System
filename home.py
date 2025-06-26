#!C:/Users/Bharathvajan/AppData/Local/Programs/Python/Python38/python.exe
import os

print("content-type:text/html \r\n\r\n ")
import pymysql, cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="amazon")
cur = con.cursor()

print("""

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Floris Knits</title>


    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
   
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
                    * {
                        margin: 0;
                        padding: 0;
                    }
            
                    .navbar {
                        background-color: rgb(241, 233, 223);
                        position: sticky;
                        top: 0;
                        left:0;
                        z-index: 2000;  
                    }
            
                    .navbar-brand {
                        font-weight: bold;
                        font-size: 1.5rem;
                        color:rgb(85, 77, 77);
                    }
            
                    .navbar-brand:hover {
                        color: rgb(85, 77, 77);
                        font-weight:bold;
                    }
            
                    .nav-link {
                        color: rgb(85, 77, 77);
                        font-weight: bold;
                        margin-right: 20px;
                        transition: color 0.3s ease, transform 0.3s ease;
                    }
            
                    .nav-link:hover {
                        color: rgb(85, 77, 77);
                        transform: scale(1.05);
                    }
            
            
                    .nav-item {
                        position: relative;
                    }
            
                    .sub-menu {
                        display: none;
                        position: absolute;
                        top: 100%;
                        left: 0;
                        background-color: rgb(241, 233, 223);
                        padding: 10px;
                        border-radius: 5px;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        min-width: 150px;
                        max-width: 250px;
                        width: 100%;
                        z-index:2000;
                        
                    }
            
                    .sub-menu a {
                        display: block;
                        color: rgb(85, 77, 77);
                        padding: 5px 10px;
                        text-decoration: none;
                    }
            
                    .sub-menu a:hover {
                        font-weight: bold;
                        color: rgb(85, 77, 77);
                    }
            
                    .sub-menu {
                        display: none;
                        position: absolute;
                        width: 100%;
                    }
            
                    .nav-item:hover .sub-menu {
                        display: flex;
                        flex-direction: column;
                    }
            
                    footer {
                        background-color: rgb(241, 233, 223);
                        padding: 30px 0;
                    }
            
                    .foot a {
                        text-decoration: none;
                        color: #3b3131;
                    }
            
                    .foot a:hover {
                        font-weight: bold;
                        transition: 0.3s;
                    }
                    .social i:hover {
                        font-weight: bold;
                        font-size:larger;
                        transition: 0.3s;
                    }
            
            
                    .social a {
                        font-size: 1.5rem;
                        margin-right: 15px;
                    }
                     
            
            
                    body {
                        overflow-x: hidden;
                    }
            
            
                    @media (max-width: 768px) {
                        footer{
                            flex-direction: column;
                            text-align: center;
                        }
                       
                    }
                       
                    .modal {
                       z-index: 6000;
            
                       }
            
            
                    section {
                        position: relative;
                        text-align: center;
                        color: white;
                    }
            
                    .bg {
                        background-image: url(image/image-from-rawpixel-id-13884982-jpeg.jpg);
                        background-size: cover;
                        background-position: center;
                        height: 660px;
            
            
                    }
                    html 
                    {
                        overflow-y: scroll;
                    }
            
            
            
            
                    .bt:hover {
                        transform: scale(1.15);
                        transition: 0.3s;
                    }
            
                    .ab {
                        position: relative;
                        top: 200px;
                    }
            
            
            
                    .about {
                        position: relative;
                        top: -5px;
                    }
            
                    .bgg {
                        background-image: url(image/fixedcone.avif);
                        background-attachment: fixed;
                        height: 500px;
            
                    }
                    .modal-content {
                    border-radius: 12px;
                    overflow: hidden;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                    }
            
            
                .modal-header {
            
                    color: black;
                    padding: 15px;
                    border-bottom: none;
                    }
            
            
            
            
                .modal-body {
                    padding: 20px;
            
                }
            
            
                .form-control {
                    border-radius: 8px;
                    border: 1px solid #ced4da;
                }
            
            
                .custom-checkbox {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    flex-wrap: wrap;
                    margin-bottom: 10px;
                }
            
                .custom-checkbox input {
                    accent-color: #343a40;
                    transform: scale(1.2);
                }
            
            
                input[type="file"] {
                    border: 1px solid #ced4da;
                    padding: 5px;
                    border-radius: 8px;
                    background-color: white;
                }
            
            
                .btn-dark {
                    background: linear-gradient(135deg, #343a40, #495057);
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                    transition: 0.3s ease-in-out;
                }
            
                .btn-dark:hover {
                    transform: scale(1.05);
                        transition: 0.3s;
                }
                .modal-content {
                    border-radius: 12px;
                    overflow: hidden;
                    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
                    border: none;
                }
            
                .modal-header {
                    background-color: #f8f5f2;
                    color: #3b3131;
                    border-bottom: 1px solid #e9e2dd;
                    padding: 16px 20px;
                }
            
                .modal-header h4, .modal-header h5 {
                    font-weight: 600;
                    margin: 0;
                }
            
                .modal-body {
                    padding: 25px;
                    background-color: #fff;
                }
            
               
                .form-control {
                    border-radius: 8px;
                    border: 1px solid #ced4da;
                    padding: 10px 15px;
                    margin-bottom: 15px;
                    transition: border-color 0.3s, box-shadow 0.3s;
                }
            
                .form-control:focus {
                    border-color: #a69b94;
                    box-shadow: 0 0 0 0.2rem rgba(166, 155, 148, 0.25);
                }
            
                .form-control.is-invalid {
                    border-color: #dc3545;
                    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
                    background-repeat: no-repeat;
                    background-position: right calc(0.375em + 0.1875rem) center;
                    background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
                }
            
                .invalid-feedback {
                    display: none;
                    color: #dc3545;
                    font-size: 0.875em;
                    margin-top: -10px;
                    margin-bottom: 10px;
                }
            
            
                .custom-checkbox {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 15px;
                    margin-bottom: 20px;
                }
            
                .checkbox-item {
                    display: flex;
                    align-items: center;
                    margin-right: 20px;
                }
            
                .checkbox-item input {
                    margin-right: 6px;
                    accent-color: #3b3131;
                }
            
            
                .modal-footer {
                    border-top: 1px solid #e9e2dd;
                    padding: 16px 20px;
                    background-color: #f8f5f2;
                }
            
                .btn-modal {
                    background: linear-gradient(135deg, #3b3131, #5c4c4c);
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                    transition: all 0.3s ease;
                    font-weight: 500;
                }
            
                .btn-modal:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    background: linear-gradient(135deg, #4d3f3f, #6d5d5d);
                }
            
                .btn-cancel {
                    background: #e9e2dd;
                    color: #3b3131;
                }
            
                .btn-cancel:hover {
                    background: #d9d2cd;
                }
            
                .account-link {
                    margin-top: 15px;
                    text-align: center;
                    font-size: 0.9rem;
                }
            
                .account-link a {
                    color: #5c4c4c;
                    text-decoration: underline;
                    font-weight: 500;
                }
            
                .account-link a:hover {
                    color: #3b3131;
                }
               
                .modal-content {
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                    border: none;
                }
                
                .modal-header {
                    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
                    background-color: #f8f9fa;
                    border-radius: 10px 10px 0 0;
                }
                
                .modal-title {
                    font-weight: 600;
                    color: #212529;
                }
                
                .form-floating > .form-control,
                .form-floating > .form-select {
                    border: 1px solid #ced4da;
                    border-radius: 6px;
                    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
                }
                
                .form-floating > .form-control:focus,
                .form-floating > .form-select:focus {
                    border-color: #80bdff;
                    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                }
                
                .form-check-input:checked {
                    background-color: #0d6efd;
                    border-color: #0d6efd;
                }
                
                .btn-dark {
                    background-color: #0d6efd;
                    border-color: #0d6efd;
                    transition: background-color 0.15s ease-in-out;
                }
                
                .btn-primary:hover {
                    background-color: #0b5ed7;
                    border-color: #0a58ca;
                }
                
                .btn-outline-secondary {
                    color: #6c757d;
                    border-color: #6c757d;
                }
                
                .btn-outline-secondary:hover {
                    color: #fff;
                    background-color:black;
                    border-color: #6c757d;
                }
            
                        
                        .invalid-feedback {
                            font-size: 0.875em;
                            color: #dc3545;
                        }
            
                        .was-validated .form-control:invalid,
                        .form-control.is-invalid {
                            border-color: #dc3545;
                            padding-right: calc(1.5em + 0.75rem);
                            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
                            background-repeat: no-repeat;
                            background-position: right calc(0.375em + 0.1875rem) center;
                            background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
                        }
            
                        
                        .modal.fade .modal-dialog {
                            transition: transform 0.3s ease-out;
                            transform: translateY(-50px);
                        }
            
                        .modal.show .modal-dialog {
                            transform: none;
                        }
            


    </style>
</head>

<body>

     <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="home.py">
                <img src="./image/textile.png" width="40px" height="40px" class="me-3">
                Floris Knits <span style="font-size: small;">Timeless Styles</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav">

                    <li class="nav-item">
                        <a class="nav-link" href="#"><i class="fa fa-user"></i> Register <i
                                class="fa fa-caret-down"></i>
                        </a>
                        <div class="sub-menu row">
                            <div class="col">
                                <a href="" data-bs-toggle="modal" data-bs-target="#myModal">Dealer</a>

                               <div class="modal fade" id="myModal">
                                <div class="modal-dialog">
                                    <div class="modal-content">

                                        
                                        <div class="modal-header">
                                            <h5 class="modal-title">Dealer Registration</h5>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal" ></button>
                                        </div>

                                        
                                        <div class="modal-body">
                                            <form method="post" name="dealerForm" id="dealerForm" enctype="multipart/form-data" onsubmit="return validateDealerForm()">
                                                <div class="row">
                                                    <div class="col-md-6 mt-4">
                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="dfname" name="dfname" placeholder="Full Name" required>
                                                            <label for="dfname">Full Name</label>
                                                            <div class="invalid-feedback" id="dfname-error">Please enter your full name</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="email" id="dmail" name="dmail" placeholder="Email" required>
                                                            <label for="dmail">Email Address</label>
                                                            <div class="invalid-feedback" id="dmail-error">Please enter a valid email address</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="dlocation" name="dlocation" placeholder="Location" required>
                                                            <label for="dlocation">Location</label>
                                                            <div class="invalid-feedback" id="dlocation-error">Please enter your location</div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6 mt-4">
                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="dbname" name="dbname" placeholder="Business Name" required>
                                                            <label for="dbname">Business Name</label>
                                                            <div class="invalid-feedback" id="dbname-error">Please enter your business name</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="tel" id="dphno" name="dphno" placeholder="Phone Number" maxlength="10" required>
                                                            <label for="dphno">Phone Number</label>
                                                            <div class="invalid-feedback" id="dphno-error">Please enter a valid 10-digit Indian phone number</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="dlno" name="dlno" placeholder="License Number" required>
                                                            <label for="dlno">License Number</label>
                                                            <div class="invalid-feedback" id="dlno-error">Please enter your license number</div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="mt-4">
                                                    <label class="form-label fw-bold">Raw Materials Provided</label>
                                                    <div class="row mt-2">
                                                        <div class="col-md-3 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="cotton" name="dmaterial" value="cotton">
                                                                <label class="form-check-label" for="cotton">Cotton</label>
                                                            </div>
                                                        </div>
                                                        <div class="col-md-3 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="rayon" name="dmaterial" value="rayon">
                                                                <label class="form-check-label" for="rayon">Rayon</label>
                                                            </div>
                                                        </div>
                                                        <div class="col-md-3 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="nylon" name="dmaterial" value="nylon">
                                                                <label class="form-check-label" for="nylon">Nylon</label>
                                                            </div>
                                                        </div>
                                                        <div class="col-md-3 mb-2">
                                                            <div class="form-check">
                                                                <input class="form-check-input" type="checkbox" id="popcorn" name="dmaterial" value="popcorn">
                                                                <label class="form-check-label" for="popcorn">Popcorn</label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="invalid-feedback" id="materials-error">Please select at least one material</div>
                                                </div>

                                                <div class="mt-4">
                                                    <label for="dimage" class="form-label fw-bold">Upload Business Logo/Image</label>
                                                    <input type="file" name="dimage" id="dimage" class="form-control" accept="image/*">
                                                    <div class="form-text">Accepted for
                                                    mats: JPG, PNG, GIF (Max size: 5MB)</div>
                                                    <div class="invalid-feedback" id="dimage-error">Please upload a valid image file</div>
                                                </div>
                                                 <div class="mt-4">
                                                    <label for="limage" class="form-label fw-bold">Upload Business License/Image</label>
                                                    <input type="file" name="limage" id="limage" class="form-control" accept="image/*">
                                                    <div class="form-text">Accepted for
                                                    mats: JPG, PNG, GIF (Max size: 5MB)</div>
                                                    <div class="invalid-feedback" id="limage-error">Please upload a valid image file</div>
                                                </div>

                                                <div class="d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                                                    <input type="submit" class="btn btn-dark btn-lg me-md-2" value="Register" name="dsubmit">
                                                    <button type="button" class="btn btn-dark btn-lg" data-bs-dismiss="modal" btn-lg me-md-2">Cancel</button>
                                                </div>

                                                <div class="text-center mt-4">
                                                    <p>Already have an account? <a href="#" data-bs-toggle="modal" data-bs-target="#dealerModal" data-bs-dismiss="modal">Login here</a></p>
                                                </div>
                                            </form>

                                        </div>
                                    </div>
                                </div>
                            </div>                      

                                <a href="wholesaler.html" data-bs-toggle="modal" data-bs-target="#wholeModal">WholeSaler</a>
                                 <div class="modal fade" id="wholeModal">
                                <div class="modal-dialog">
                                    <div class="modal-content">

                                        
                                        <div class="modal-header">
                                            <h5 class="modal-title">Wholesaler Registration</h5>
                                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                                        </div>

                                       
                                        <div class="modal-body">
                                            <form method="post" name="dealerForm" id="wholeForm" enctype="multipart/form-data" onsubmit="return validatewholeForm()">
                                                <div class="row">
                                                    <div class="col-md-6 mt-4">
                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="wfname" name="wfname" placeholder="Full Name" required>
                                                            <label for="wfname">Full Name</label>
                                                            <div class="invalid-feedback" id="wfname-error">Please enter your full name</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="email" id="dmail" name="wmail" placeholder="Email" required>
                                                            <label for="wmail">Email Address</label>
                                                            <div class="invalid-feedback" id="wmail-error">Please enter a valid email address</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="wlocation" name="wlocation" placeholder="Location" required>
                                                            <label for="wlocation">Location</label>
                                                            <div class="invalid-feedback" id="wlocation-error">Please enter your location</div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6 mt-4">
                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="wbname" name="wbname" placeholder="Business Name" required>
                                                            <label for="wbname">Business Name</label>
                                                            <div class="invalid-feedback" id="wbname-error">Please enter your business name</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="tel" id="wphno" name="wphno" placeholder="Phone Number" maxlength="10" required>
                                                            <label for="wphno">Phone Number</label>
                                                            <div class="invalid-feedback" id="wphno-error">Please enter a valid 10-digit Indian phone number</div>
                                                        </div>

                                                        <div class="form-floating mb-3">
                                                            <input class="form-control" type="text" id="wlno" name="wlno" placeholder="License Number" required>
                                                            <label for="wlno">License Number</label>
                                                            <div class="invalid-feedback" id="wlno-error">Please enter your license number</div>
                                                        </div>
                                                    </div>
                                                </div>


                                                <div class="mt-4">
                                                    <label for="wimage" class="form-label fw-bold">Upload Business Logo/Image</label>
                                                    <input type="file" name="wimage" id="wimage" class="form-control" accept="image/*">
                                                    <div class="form-text">Accepted formats: JPG, PNG, GIF (Max size: 5MB)</div>
                                                    <div class="invalid-feedback" id="wimage-error">Please upload a valid image file</div>
                                                </div>
                                                <div class="mt-4">
                                                    <label for="wlimage" class="form-label fw-bold">Upload Business License/Image</label>
                                                    <input type="file" name="wlimage" id="wlimage" class="form-control" accept="image/*">
                                                    <div class="form-text">Accepted for
                                                    mats: JPG, PNG, GIF (Max size: 5MB)</div>
                                                    <div class="invalid-feedback" id="wlimage-error">Please upload a valid image file</div>
                                                </div>

                                                <div class="d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                                                    <input type="submit" class="btn btn-dark btn-lg me-md-2" value="Register" name="wsubmit">
                                                    <button type="button" class="btn btn-dark btn-lg" data-bs-dismiss="modal" btn-lg me-md-2">Cancel</button>
                                                </div>

                                                <div class="text-center mt-4">
                                                    <p>Already have an account? <a href="#" data-bs-toggle="modal" data-bs-target="#dealerModal" data-bs-dismiss="modal">Login here</a></p>
                                                </div>
                                            </form>

                                        </div>
                                    </div>
                                </div>
                            </div>         

                            </div>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><img src="./image/enter.png" height="15px" width="17px"> Login <i
                                class="fa fa-caret-down"></i></a>
                        <div class="sub-menu row">
                            <div class="col">

                                <a href="ad.py" data-bs-toggle="modal" data-bs-target="#adModal">Admin</a>
                                <div class="modal" id="adModal">
                                    <div class="modal-dialog">
                                        <div class="modal-content" >


                                            <div class="modal-header">
                                                <center><h4 class="modal-title">Admin Login </h4></center>
                                                <button type="button" class="btn-close"
                                                    data-bs-dismiss="modal"></button>
                                            </div>


                                            <div class="modal-body" >
                                                <form method="post" name="form" enctype="multipart/form-data">
                                                    <input class="form-control text-dark" type="text" name="adname" placeholder="Username" required>
                                                    <br>
                                                    <div class="position-relative">
                                                        <input class="form-control text-dark pr-5" type="password" name="adpass" placeholder="Password" id="currentPassword" required>
                                                        <i class="password-toggle fas fa-eye position-absolute" 
                                                           style="top: 50%; right: 10px; transform: translateY(-50%); cursor: pointer;"
                                                           onclick="togglePasswordVisibility('currentPassword', this)">
                                                        </i>
                                                    </div>

                                                    <br>
                                                    <center>
                                                    <input type="submit" class="btn btn-dark me-3" value="Login" name="adsubmit">  <button type="button" class="btn btn-dark"
                                                    data-bs-dismiss="modal" >Cancel</button></center>


                                                </form>



                                            </div>

                                        </div>
                                    </div>
                                </div>

                                <a href="" data-bs-toggle="modal" data-bs-target="#adminModal">Owner</a>

                                <div class="modal" id="adminModal">
                                    <div class="modal-dialog">
                                        <div class="modal-content" >


                                            <div class="modal-header">
                                                <center><h4 class="modal-title">Owner Login </h4></center>
                                                <button type="button" class="btn-close"
                                                    data-bs-dismiss="modal"></button>
                                            </div>


                                            <div class="modal-body" >
                                                <form method="post" name="form" enctype="multipart/form-data">
                                                    <input class="form-control text-dark" type="text" name="uname" placeholder="Username" required>
                                                    <br>


                                                     <div class="position-relative">
                                                        <input class="form-control text-dark pr-5" type="password" name="pass" placeholder="Password" id="currentPass" required>
                                                        <i class="password-toggle fas fa-eye position-absolute" 
                                                           style="top: 50%; right: 10px; transform: translateY(-50%); cursor: pointer;"
                                                           onclick="togglePassword('currentPass', this)">
                                                        </i>
                                                    </div>
                                                    <center>
                                                    <input type="submit" class="btn btn-dark me-3" value="Login" name="submit">  <button type="button" class="btn btn-dark"
                                                    data-bs-dismiss="modal" >Cancel</button></center>


                                                </form>



                                            </div>

                                        </div>
                                    </div>
                                </div>

                                <a href="" data-bs-toggle="modal" data-bs-target="#dealerModal">Dealer
                                </a>
                                 <div class="modal" id="dealerModal" >
                                    <div class="modal-dialog">
                                        <div class="modal-content" >


                                            <div class="modal-header">
                                                <center><h4 class="modal-title">Dealer Login </h4></center>
                                                <button type="button" class="btn-close"
                                                    data-bs-dismiss="modal"></button>
                                            </div>


                                            <div class="modal-body" >
                                                <form method="post" name="form" enctype="multipart/form-data">
                                                    <input class="form-control text-dark" type="text" name="rlname" placeholder="Username" required>
                                                    <br>

                                                    <div class="position-relative">
                                                        <input class="form-control text-dark pr-5" type="password" name="rlpass" placeholder="Password" id="currentP" required>
                                                        <i class="password-toggle fas fa-eye position-absolute" 
                                                           style="top: 50%; right: 10px; transform: translateY(-50%); cursor: pointer;"
                                                           onclick="toggleP('currentP', this)">
                                                        </i>
                                                    </div>
                                                    <br>
                                                    <center>
                                                    <input type="submit" class="btn btn-dark me-3" value="Login" name="rlsubmit">  <button type="button" class="btn btn-dark"
                                                    data-bs-dismiss="modal" >Cancel</button></center>  <br>

                                                    <div class="d-flex"><p class="me-4">Don't Have an account?</p><a href="home.py" >Register</a></div>
                                                </form> 
                                            </div>

                                        </div>
                                    </div>
                                </div>
                                <a href="" data-bs-toggle="modal" data-bs-target="#ManagerModal">Manager
                                </a>
                                <div class="modal" id="ManagerModal" >
                                    <div class="modal-dialog">
                                        <div class="modal-content" >


                                            <div class="modal-header">
                                                <center><h4 class="modal-title">Manager Login </h4></center>
                                                <button type="button" class="btn-close"
                                                    data-bs-dismiss="modal"></button>
                                            </div>


                                            <div class="modal-body" >
                                                <form method="post" name="form" enctype="multipart/form-data">
                                                    <input class="form-control text-dark" type="text" name="mname" placeholder="Username" required>
                                                    <br>

                                                    <div class="position-relative">
                                                        <input class="form-control text-dark pr-5" type="password" name="mpass" placeholder="Password" id="currentPas" required>
                                                        <i class="password-toggle fas fa-eye position-absolute" 
                                                           style="top: 50%; right: 10px; transform: translateY(-50%); cursor: pointer;"
                                                           onclick="togglePas('currentPas', this)">
                                                        </i>
                                                    </div>
                                                    <br>
                                                    <center>
                                                    <input type="submit" class="btn btn-dark me-3" value="Login" name="msubmit">  <button type="button" class="btn btn-dark"
                                                    data-bs-dismiss="modal" >Cancel</button></center>  <br>


                                                </form> 
                                            </div>

                                        </div>
                                    </div>
                                </div>

                                <a href="" data-bs-toggle="modal" data-bs-target="#lwholeModal">WholeSaler</a>
                                <div class="modal" id="lwholeModal" >
                                    <div class="modal-dialog">
                                        <div class="modal-content" >


                                            <div class="modal-header">
                                                <center><h4 class="modal-title">Wholesaler Login </h4></center>
                                                <button type="button" class="btn-close"
                                                    data-bs-dismiss="modal"></button>
                                            </div>


                                            <div class="modal-body" >
                                                <form method="post" name="form" enctype="multipart/form-data">
                                                    <input class="form-control text-dark" type="text" name="wholename" placeholder="Username" required>
                                                    <br>

                                                    <div class="position-relative">
                                                        <input class="form-control text-dark pr-5" type="password" name="wholepass" placeholder="Password" id="current" required>
                                                        <i class="password-toggle fas fa-eye position-absolute" 
                                                           style="top: 50%; right: 10px; transform: translateY(-50%); cursor: pointer;"
                                                           onclick="togglepa('current', this)">
                                                        </i>
                                                    </div>
                                                    <br>
                                                    <center>
                                                    <input type="submit" class="btn btn-dark me-3" value="Login" name="wholesubmit">  <button type="button" class="btn btn-dark"
                                                    data-bs-dismiss="modal" >Cancel</button></center>  <br>

                                                    <div class="d-flex"><p class="me-4">Don't Have an account?</p><a href="home.py" >Register</a></div>
                                                </form> 
                                            </div>

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="about.py"></i> About Us</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="contact.py"><i class="fa fa-phone"></i> Contact Us</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <section>
        <div>
            <div class="bg">
                <div class="ab" data-aos="zoom-in">

                    <h1
                        style=" font-family:Georgia, 'Times New Roman', Times, serif;color: rgba(53, 5, 5, 0.647); font-size:50px;font-weight: bold;">
                        STITCHING DREAMS, <br><br>WEAVING MAGIC
                    </h1><br>

                    </h4><br><br>

                </div>

            </div>
        </div>
        <div class="about p-5 container-fluid bg-dark">
            <div class="row ">
                <div class="col-md-1"></div>
                <div class="col-md-5">

                    <div id="demo" class="carousel slide" data-bs-ride="carousel">


                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
                            <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
                            <button type="button" data-bs-target="#demo" data-bs-slide-to="2"></button>
                        </div>

                        <!-- The slideshow/carousel -->
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img src="./image/11062b_cdc478cbf9914f968666f48ca5749fc1~mv2_d_5820_3880_s_4_2.avif"
                                    alt="Los Angeles" class="d-block w-100" height="550px">
                            </div>
                            <div class="carousel-item">
                                <img src="image/11062b_354b515b7bbe41139151655383eac04d~mv2.avif" alt="Chicago"
                                    class="d-block w-100" height="550px">
                            </div>
                            <div class="carousel-item">
                                <img src="image/sew-8353303.jpg" alt="New York" class="d-block w-100" height="550px">
                            </div>
                        </div>

                        <!-- Left and right controls/icons -->
                        <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon"></span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
                            <span class="carousel-control-next-icon"></span>
                        </button>
                    </div>
                    <img src="./image/BC bar.avif" class="process c" data-aos="fade-up">

                </div>



                <div class="col-md-1"></div>
                <div class="col-md-4 mt-4">
                    <h2 class="typing-text" data-aos="fade-up">WHO WE ARE? </h2><br><br><br>

                    <b style="color:rgb(236, 230, 230);font-family: Arial, Helvetica, sans-serif;"
                        data-aos="fade-up">With a Production of more than lakhs of products in a year,
                        Floris Knits is the largest vertically integrated
                        textile manufacturer in Tiruppur.One thing that has anchored Floris Knit's growth over a decades
                        of an ever evolving, complex,
                        cyclical and often disruptive business environment is the unwavering pursuit of excellence.We
                        envision revolutionizing the industry through innovation, sustainability,
                        and exceptional customer service.

                    </b><br><br><br><br>
                    <img src="./image/about-14.png" data-aos="fade-down">
                    <img src="image/photo-gallery-ele2.png" data-aos="fade-down">
                    <img src="image/abt-flower2.png" data-aos="fade-down">







                </div>
            </div>
        </div><br><br><br><br><br><br>
        <div class="cone container">
            <div class="row">
                <div class="col-md-1"></div>

                <div class="col-md-2 co mt-4">
                    <img src="./image/Customer.png" alt="" height="300px" width="200px" data-aos="fade-up"><br><br><br>
                    <p class="text-secondary mt-4" data-aos="fade-up">Understand, engage, and deliver with total
                        customer focus in all
                        operational areas</p>
                </div>
                <div class="col-md-1"></div>



                <div class="col-md-2 co mt-4">
                    <img src="./image/Quality.png" alt="" height="300px" width="200px" data-aos="fade-up"><br><br><br>
                    <p class="text-secondary mt-4" data-aos="fade-up">Ensure the best quality through latest technology,
                        well-structured
                        and
                        standardised work practices</p>
                </div>
                <div class="col-md-1"></div>

                <div class="col-md-2 co mt-4">
                    <img src="./image/Respact.png" alt="" height="300px" width="200px" data-aos="fade-up"><br><br><br>
                    <p class="text-secondary mt-4" data-aos="fade-up">Faith in individual potential and respect for
                        human values</p>
                </div>
                <div class="col-md-1"></div>
                <div class="col-md-2 co mt-4">
                    <img src="./image/Innovation.png" alt="" height="300px" width="200px"
                        data-aos="fade-up"><br><br><br>
                    <p class="text-secondary mt-4" data-aos="fade-up">Be a responsible corporate citizen and positively
                        contribute to the
                        society that we live in</p>
                </div>

            </div>

        </div>

        <br><br><br><br>
        <div class="container">
            <div class="row">
                <div class="col-md-1">
                    <img src="./image/Vision (1).svg" data-aos="fade-up" height="200px" width="200px">
                </div>
                <div class="col-md-5">
                    <h2 data-aos="fade-up" style="color:  #460a0a;">VISION</h2><br>
                    <h5 class="text-dark" style="text-indent: 70px;" data-aos="fade-up">Rooted in Values,
                        Creating World Class Textiles</h5>

                </div>
                <div class="col-md-1">
                    <img src="./image/Mission.svg" data-aos="fade-up" height="200px" width="200px">
                </div>
                <div class="col-md-5">
                    <h2 data-aos="fade-up" style="color:  #460a0a;">MISSION</h2><br>
                    <h5 class="text-dark" style="text-indent: 70px;;" data-aos="fade-up">The aim is
                        producing diverse products for the global textiles.</h5>

                </div>
            </div>

        </div>
        <div class="bgg mt-4">
            <h2 style="position: relative;top: 200px;color: #ffffff;font-weight: bolder">Quality Is Our Priority</h2>
        </div>
        <br><br><br>
        <br><br>
        <div class="container">
            <h2 style="color: #460a0a;" data-aos="fade-up">Fabric Types Available</h2> <br><br><br>
            <br><br>
            <div class="row">
                <div class="col-md-1"></div>
                
                <div class="col-md-1 mt-4"></div>
                <div class="col-md-1">
                    <img src="./image/Nylon-800x667.jpg" class="rounded-circle" height="150px" width="150px"
                        data-aos="fade-up"><br><br>
                    <h4 style="color: #3f3c3c;text-indent: 13px;" data-aos="fade-up">Lycra</h4>
                </div>
                <div class="col-md-1 mt-4"></div>
                <div class="col-md-1">
                    <img src="./image/Rayon-800x667.jpg" class="rounded-circle" height="150px" width="150px"
                        data-aos="fade-up"><br><br>
                    <h4 style="color: #3f3c3c;text-indent: 28px;" data-aos="fade-up">Rayon</h4>
                </div>
                <div class="col-md-1 mt-4 "></div>
                <div class="col-md-1">
                    <img src="./image/APS8390_1_360x.jpg" class="rounded-circle" height="150px" width="150px"
                        data-aos="fade-up"><br><br>
                    <h4 style="color: #3f3c3c;text-indent: 32px;" data-aos="fade-up">Cotton</h4>
                </div>
                <div class="col-md-1 mt-4"></div>
                <div class="col-md-1">
                    <img src="./image/images (6).jpeg" class="rounded-circle" height="150px" width="150px"
                        data-aos="fade-up"><br><br>
                    <h4 style="color: #3f3c3c;text-indent: 25px;" data-aos="fade-up">Popcorn</h4>
                </div>
                <div class="col-md-1"></div>

            </div>
        </div>
        <div><br><br><br><br><br>
        <h3 style="color:black;" class="mt-4 mb-4">Products Manufacturing</h3><br><br><br>
        <div class="row mt-4">
                <div class="col-md-3"></div>
                
                <div class="col-md-1 mt-4"></div>
                <div class="col-md-1">
                    <img src="./image/sara.avif"  height="250px" width="250px"
                        data-aos="fade-up"><br><br>
                    
                </div>
                <div class="col-md-1 mt-4"></div>
                <div class="col-md-1">
                    <img src="./image/saa.avif"  height="250px" width="250px"
                        data-aos="fade-up"><br><br>
                    
                </div>
                <div class="col-md-4 mt-4 "></div>

        </div>
        
        </div>
        
        



    </section>

    <footer class="mt-4">
  <div class="container">
    <div class="row text-center text-md-start">
      <!-- Useful Links Section -->
      <div class="col-md-4 mb-4">
        <h5 style="color: #460a0a;">Useful Links</h5>
        <ul class="list-unstyled foot">
          <li><a href="about.py">About Us</a></li>
          <li><a href="contact.py">Contact Us</a></li>
        </ul>
      </div>

      <!-- Follow Us Section -->
      <div class="col-md-4 mb-4">
        <h5 style="color: #460a0a;">Follow Us</h5>
        <div class="d-flex justify-content-center justify-content-md-start social">
          <a href="https://www.facebook.com/floris" target="_blank" class="me-3"><i class="fa-brands fa-facebook" style="color:grey;"></i></a>
          <a href="https://twitter.com/floris" target="_blank" class="me-3"><i class="fa-brands fa-twitter" style="color:grey;"></i></a>
          <a href="https://www.instagram.com/floris" target="_blank"><i class="fa-brands fa-instagram" style="color:grey;"></i></a>
        </div>
      </div>

      <!-- Contact Section -->
      <div class="col-md-4 mb-4">
        <h5 style="color: #460a0a;">Contact</h5>
        <ul class="list-unstyled">
          <li>Phone: 986574893</li>
          <li>Mail: florisknits@gmail.com</li>
        </ul>
      </div>
    </div>

    <!-- Back to Top Button -->
    <div class="text-center mt-4">
      <a href="#" class="btn btn-dark">Back to Top</a>
    </div>
  </div>
</footer>



    <script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
    <script>
        AOS.init({
            duration: 1000,
            easing: 'ease-in-out',
            once: true
        });

                function validateDealerForm() {
                    let isValid = true;


                    document.querySelectorAll('.is-invalid').forEach(el => {
                        el.classList.remove('is-invalid');
                    });


                    const fullName = document.getElementById('dfname');
                    if (!fullName.value || fullName.value.trim().length < 3) {
                        fullName.classList.add('is-invalid');
                        document.getElementById('dfname-error').textContent = "Please enter a valid full name (minimum 3 characters)";
                        isValid = false;
                    }


                    const email = document.getElementById('dmail');
                    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
                    if (!emailRegex.test(email.value)) {
                        email.classList.add('is-invalid');
                        document.getElementById('dmail-error').textContent = "Please enter a valid email address";
                        isValid = false;
                    }


                    const location = document.getElementById('dlocation');
                    if (!location.value || location.value.trim().length < 3) {
                        location.classList.add('is-invalid');
                        document.getElementById('dlocation-error').textContent = "Please enter a valid location";
                        isValid = false;
                    }


                    const businessName = document.getElementById('dbname');
                    if (!businessName.value || businessName.value.trim().length < 2) {
                        businessName.classList.add('is-invalid');
                        document.getElementById('dbname-error').textContent = "Please enter a valid business name";
                        isValid = false;
                    }


                    const phone = document.getElementById('dphno');
                    const phoneRegex = /^[6-9]\d{9}$/;
                    if (!phoneRegex.test(phone.value)) {
                        phone.classList.add('is-invalid');
                        document.getElementById('dphno-error').textContent = "Please enter a valid 10-digit Indian phone number (starting with 6, 7, 8, or 9)";
                        isValid = false;
                    }


                    const licenseNumber = document.getElementById('dlno');
                    if (!licenseNumber.value || licenseNumber.value.trim().length < 5) {
                        licenseNumber.classList.add('is-invalid');
                        document.getElementById('dlno-error').textContent = "Please enter a valid license number (minimum 5 characters)";
                        isValid = false;
                    }


                    const materials = document.querySelectorAll('input[name="dmaterial"]:checked');
                    if (materials.length === 0) {
                        document.getElementById('materials-error').style.display = 'block';
                        isValid = false;
                    } else {
                        document.getElementById('materials-error').style.display = 'none';
                    }


                    const imageInput = document.getElementById('dimage');
                    if (imageInput.files.length > 0) {
                        const file = imageInput.files[0];
                        const validImageTypes = ['image/jpeg', 'image/png', 'image/gif'];
                        const maxSize = 5 * 1024 * 1024; // 5MB

                        if (!validImageTypes.includes(file.type)) {
                            imageInput.classList.add('is-invalid');
                            document.getElementById('dimage-error').textContent = "Please select a valid image file (JPG, PNG, GIF)";
                            isValid = false;
                        } else if (file.size > maxSize) {
                            imageInput.classList.add('is-invalid');
                            document.getElementById('dimage-error').textContent = "Image file is too large (maximum 5MB)";
                            isValid = false;
                        }
                    }

                    return isValid;
                }


                document.getElementById('dphno').addEventListener('input', function(e) {

                    this.value = this.value.replace(/\D/g, '');


                    if (this.value.length > 10) {
                        this.value = this.value.slice(0, 10);
                    }
                });
                 function validatewholeForm() {
                    let isValid = true;


                    document.querySelectorAll('.is-invalid').forEach(el => {
                        el.classList.remove('is-invalid');
                    });


                    const fullname = document.getElementById('wfname');
                    if (!fullname.value || fullname.value.trim().length < 3) {
                        fullname.classList.add('is-invalid');
                        document.getElementById('wfname-error').textContent = "Please enter a valid full name (minimum 3 characters)";
                        isValid = false;
                    }


                    const mail = document.getElementById('wmail');
                    const mailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
                    if (!mailRegex.test(mail.value)) {
                        mail.classList.add('is-invalid');
                        document.getElementById('wmail-error').textContent = "Please enter a valid email address";
                        isValid = false;
                    }


                    const loc = document.getElementById('wlocation');
                    if (!loc.value || loc.value.trim().length < 3) {
                        loc.classList.add('is-invalid');
                        document.getElementById('wlocation-error').textContent = "Please enter a valid location";
                        isValid = false;
                    }


                    const business = document.getElementById('wbname');
                    if (!business.value || business.value.trim().length < 2) {
                        business.classList.add('is-invalid');
                        document.getElementById('wbname-error').textContent = "Please enter a valid business name";
                        isValid = false;
                    }


                    const pno = document.getElementById('wphno');
                    const pnoRegex = /^[6-9]\d{9}$/;
                    if (!pnoRegex.test(phone.value)) {
                        pno.classList.add('is-invalid');
                        document.getElementById('wphno-error').textContent = "Please enter a valid 10-digit Indian phone number (starting with 6, 7, 8, or 9)";
                        isValid = false;
                    }


                    const licenseNo = document.getElementById('wlno');
                    if (!licenseNo.value || licenseNo.value.trim().length < 5) {
                        licenseNo.classList.add('is-invalid');
                        document.getElementById('wslno-error').textContent = "Please enter a valid license number (minimum 5 characters)";
                        isValid = false;
                    }





                    const wimageInput = document.getElementById('wimage');
                    if (wimageInput.files.length > 0) {
                        const file = wimageInput.files[0];
                        const wvalidImageTypes = ['image/jpeg', 'image/png', 'image/gif'];
                        const maxSize = 5 * 1024 * 1024; // 5MB

                        if (!wvalidImageTypes.includes(file.type)) {
                            wimageInput.classList.add('is-invalid');
                            document.getElementById('wimage-error').textContent = "Please select a valid image file (JPG, PNG, GIF)";
                            isValid = false;
                        } else if (file.size > maxSize) {
                            wimageInput.classList.add('is-invalid');
                            document.getElementById('wimage-error').textContent = "Image file is too large (maximum 5MB)";
                            isValid = false;
                        }
                    }

                    return isValid;
                }


                document.getElementById('wphno').addEventListener('input', function(e) {

                    this.value = this.value.replace(/\D/g, '');


                    if (this.value.length > 10) {
                        this.value = this.value.slice(0, 10);
                    }
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
                function togglePassword(inputId, icon) {
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
               function toggleP
               (inputId, icon) {
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
               function togglepa
               (inputId, icon) {
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
               function togglepas
               (inputId, icon) {
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
""")

forms = cgi.FieldStorage()
rdname = forms.getvalue("dfname")
business = forms.getvalue("dbname")
rdmail = forms.getvalue("dmail")
rdphno = forms.getvalue("dphno")
rdloc = forms.getvalue("dlocation")
rdlno = forms.getvalue("dlno")
rdmat = forms.getlist("dmaterial")
rdimage = forms.getvalue("dimage")
rdsubmit = forms.getvalue("dsubmit")

id = forms.getvalue("id")
submit = forms.getvalue("submit")

rldname = forms.getvalue("rlname")
rldpass = forms.getvalue("rlpass")
rldsubmit = forms.getvalue("rlsubmit")

if rdsubmit != None:
    check_email_query = "SELECT email FROM dealer WHERE email = '%s'" % (rdmail)
    cur.execute(check_email_query)
    existing_email = cur.fetchone()

    if existing_email:

        print("""
            <script>
            alert("This email is already registered. Please use a different email address.");
            </script>
            """)
    else:
        rdimage = forms['dimage']
        fn = os.path.basename(rdimage.filename)
        open("images/" + fn, "wb").write(rdimage.file.read())

        rlimage = forms['limage']
        fnn = os.path.basename(rlimage.filename)
        open("images/" + fn, "wb").write(rlimage.file.read())

        x = """insert into dealer(full_Name,business_Name,email,phone,location,license_No,raw_Materials,image,status,username,password,liimage) values('%s','%s','%s','%s','%s','%s','%s','%s','False','','','%s')""" % (
            rdname, business, rdmail, rdphno, rdloc, rdlno, ','.join(rdmat),fn,fnn)
        cur.execute(x)
        con.commit()
        print("""

        <script>
        alert("Registered Sucessfully")
        </script>"""
              )





wname = forms.getvalue("wfname")
wbusiness = forms.getvalue("wbname")
wemail = forms.getvalue("wmail")
wphone = forms.getvalue("wphno")
wloc = forms.getvalue("wlocation")
wslno = forms.getvalue("wlno")


wssubmit = forms.getvalue("wsubmit")

id = forms.getvalue("id")
submit = forms.getvalue("submit")




if wssubmit != None:
    cm = "SELECT mail FROM wholesaler WHERE mail = '%s'" % (wemail)
    cur.execute(cm)
    em = cur.fetchone()

    if em:

        print("""
            <script>
            alert("This email is already registered. Please use a different email address.");
            </script>
            """)
    else:
        wsimage = forms['wimage']
        fn = os.path.basename(wsimage.filename)
        open("images/" + fn, "wb").write(wsimage.file.read())
        wslimage = forms['wlimage']
        fnn = os.path.basename(wslimage.filename)
        open("images/" + fn, "wb").write(wslimage.file.read())

        w = """insert into wholesaler(fullname,	business_name,mail,phno,location,license,status,image,liimg) values('%s','%s','%s','%s','%s','%s',"False",'%s','%s')""" % (
            wname, wbusiness, wemail, wphone, wloc,wslno,fn,fnn)
        cur.execute(w)
        con.commit()
        print("""

        <script>
        alert("Registered Sucessfully")
        </script>"""
              )










auser = forms.getvalue("adname")
apassword = forms.getvalue("adpass")
asubmit=forms.getvalue("adsubmit")

if asubmit != None:
    s = """select id from ad where username='%s' and password='%s' """ % (auser, apassword)
    cur.execute(s)
    res = cur.fetchone()
    if res != None:
        print("""
        <script>
        alert("login success")
        location.href="ad.py?id=%s"
        </script>

        """ % (res[0]))
    else:
        print("""
        <script>
        alert("Incorrect password or user name")
        location.href="home.py"
        </script>
        """)




user = forms.getvalue("uname")
password = forms.getvalue("pass")

if submit != None:
    q = """select Id from admin where username='%s' and password='%s' """ % (user, password)
    cur.execute(q)
    res = cur.fetchone()
    if res != None:
        print("""
        <script>
        alert("login success")
        location.href="admin_dashboard.py?id=%s"
        </script>

        """ % (res[0]))
    else:
        print("""
        <script>
        alert("Incorrect password or user name")
        location.href="home.py"
        </script>
        """)

if rldsubmit != None:
    q = """select Id from dealer where username='%s' and password='%s' """ % (rldname, rldpass)
    cur.execute(q)
    rel = cur.fetchone()
    if rel != None:
        print("""
        <script>
        alert("login success")
        location.href="dealer_dashboard.py?id=%s"
        </script>

        """ % (rel[0]))
    else:
        print("""
        <script>
        alert("Incorrect password or user name")
        location.href="home.py"
        </script>
        """)

wsrname=forms.getvalue("wholename")
wsrpass=forms.getvalue("wholepass")
wsrsubmit=forms.getvalue("wholesubmit")

if wsrsubmit != None:
    wl = """select id from wholesaler where username='%s' and password='%s' """ % (wsrname, wsrpass)
    cur.execute(wl)
    rel = cur.fetchone()
    if rel != None:
        print("""
        <script>
        alert("login success")
        location.href="wholesaler_dashboard.py?id=%s"
        </script>

        """ % (rel[0]))
    else:
        print("""
        <script>
        alert("Incorrect password or user name")
        location.href="home.py"
        </script>
        """)


muser = forms.getvalue("mname")
mpassword = forms.getvalue("mpass")
mansubmit=forms.getvalue("msubmit")
if mansubmit!=None:
    m = """select id from manager where username='%s' and password='%s' """ % (muser, mpassword)
    cur.execute(m)
    rel = cur.fetchone()
    if rel != None:
        print("""
           <script>
           alert("login success")
           location.href="manager_dashboard.py?id=%s"
           </script>

           """ % (rel[0]))
    else:
        print("""
           <script>
           alert("Incorrect password or user name")
           location.href="home.py"
           </script>
           """)
