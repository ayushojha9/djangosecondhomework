from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    html = "<html><body><h1>hello world</h1></body></html>"
    return HttpResponse(html)


def about (request):
    html = "<html><body><h1>this is about page</h1></body></html>"
    return HttpResponse(html)


def blog (request):
    html = "<html><body><h1>this is blog page</h1></body></html>"
    return HttpResponse(html)

def login (request):
    html = "<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/register.css">
</head>
  <!-- HEADER SECTION START-->
  <body>
  <section class="header_section">
    <div class="container">
        <div class="header_box">
            <div class="header_logo">
                <a href="#">PYTHO LAB</a>
            </div>
            <div class="header_btn">
                <ul>
                    <li><a href="login.html">Login</a></li>
                    <li><a href="register.html">Register</a></li>
                </ul>
            </div>
        </div>
    </div>
</section>
<!-- HEADER SECTION END-->
<!--Middle part start-->
<section class="Middle">
    <div class="container">
        <div class="box">
            <div class="box_content">
           
               <div class="form_box">
                   <div class="form_heading">
                       <h1>REGISTER</h1>
                       </div>
                       <div class="form">
                        <div class="input_box">
                            <input type="email" class="form_design" placeholder="Email Address"
                                onfocus="this.placeholder=''" onblur="this.placeholder='Email Address'">
                        </div>
                        <div class="input_box">
                            <input type="password" class="form_design" placeholder="Password"
                                onfocus="this.placeholder=''" onblur="this.placeholder='Password'">
                        </div>
                        <div class="input_box">
                            <input type="confirm_password" class="form_design" placeholder="Confirm Password"
                                onfocus="this.placeholder=''" onblur="this.placeholder='Comfirm Password'">
                        </div>
                        <div class="input_box links">
                            <div class="linktext">
                                <a href="#">Forget Password?</a>
                            </div>
                            <span>or</span>
                            <div class="linktext">
                                <a href="#">Register a new Account</a>
                            </div>
                        </div>
                        <div class="input_box">
                            <input type="submit" value="Register" class="login_btn">
                        </div>
                      </div> 
             </div>
          </div>
        </div>
    </div>

    
</section>
 <section class="footer_section">
        <div class="container">
            <div class="footer_box">
                <div class="footer_text">
                    <span>Designed By</span>
                    <a href="#">Indesign Media</a>
                </div>
            </div>
        </div>
    </section>
</body>
</html>"
    return HttpResponse(html)