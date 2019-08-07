from django.shortcuts import render, HttpResponse, redirect
from user.form import user_info_form
from user.models import user_info
from django.core.files.storage import FileSystemStorage
from miscellaneous.otp_sending import otp_sending, time_gen
from miscellaneous.smtp import smtp
from miscellaneous.smtp2 import smtp2
from miscellaneous.autherize import autherize
from django.contrib.auth.hashers import make_password,check_password


def signup(request):
    if request.method == "POST":
        user_image = None
        if request.FILES:
            myfile = request.FILES["user_image"]
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            user_image = fs.url(filename)
            user_image = myfile.name

        form = user_info_form(request.POST)
        f = form.save(commit=False)

        role_id_1 = request.POST["User_Type"]
        role_id = int(role_id_1)
        #f.address = request.POST["address"]

        if role_id == 2:

            f.image = user_image
            f.first_name = request.POST["first_name"]  # column name
            f.last_name = request.POST["last_name"]
            f.email = request.POST["email"]
            f.password = make_password(request.POST["confirm_password"])
            f.mobile_no = request.POST["mobile_no"]
            f.app_id_id = 6
            f.roleid_id = 2
            f.otp = otp_sending()  # column name =
            f.otp_gen_time = time_gen()
            time = "%s%s" % (time_gen())
            token = f.otp+time
            x = "%s %s" % (f.first_name, f.last_name)
            link = 'http://127.0.0.1:8000/user/activeuser/?token='+str(token)+'&email='+request.POST["email"]

            f.token = token
            smtp(x, link, f.otp_gen_time, f.email)

            f.save()
            return HttpResponse("<h1> VERIFY THE USER , SEE YOUR EMAIL </h1>")

        if role_id == 3:

            f.image = user_image
            f.first_name = request.POST["first_name"]  # column name
            f.last_name = request.POST["last_name"]
            f.email = request.POST["email"]
            f.password = make_password(request.POST["confirm_password"])
            f.mobile_no = request.POST["mobile_no"]
            f.roleid_id = 3
            f.app_id_id = request.POST["business"]
            f.business_user_business_info = request.POST["message"]
            f.save()
            return HttpResponse("<h1> After verify all details your account is activated ,you will get an mail on confirmation</h1>")

    return render(request, "signup.html")

def login(request):

    if request.method == "POST":
        un = request.POST["email"]
        up = request.POST["password"]
        try:
            data = user_info.objects.get(email=un)

        except:

            return render(request, "userlogin.html", {'emailerror': True})

        dp1 = data.password
        dp = check_password(up, dp1)
        r_id = data.roleid_id

        active = data.isactive

        if (active == False):
            return render(request, "userlogin.html", {'activeerror': True})

        else:
            if (dp == True):
                if r_id == 2:

                    request.session['Authentication'] = True
                    request.session['emailid'] = un
                    data = user_info.objects.get(email=un)
                    request.session['role'] = data.roleid_id

                    return redirect("/user/signup/")
                else:
                    request.session['Authentication'] = True
                    request.session['emailid'] = un
                    d2 = user_info.objects.get(email=un)

                    return render(request, "hotelindex.html", {"ud": d2})
            else:
                return render(request, "userlogin.html", {'passworderror': True})

    return render(request, "userlogin.html")

def verifyuser(request):

    token = request.GET["token"]
    email = request.GET["email"]
    data = user_info.objects.get(email=email)
    print(data)

    tokenvalue = data.token

    print(tokenvalue)

    if (token == tokenvalue ):
        update = user_info(
            email=email,
            isactive=True
        )
        update.save(update_fields=["isactive"])

        return HttpResponse("<h1>you have sucessfully added  </h1>")

    else:
       return HttpResponse("<h1>not verified </h1>")


def update_password(request):

    if request.method == "POST":

        un = request.POST["email"]

        try:
            data = user_info.objects.get(email=un)
            active = data.isactive

            if (active == False):
                return render(request, "userlogin.html", {'activeerror': True})

            request.session['emailid'] = un
            request.session['Authentication'] = True
            return redirect("/user/forgetpassword2page/")

        except:
            return render(request, "forget_password_email.html", {'emailerror': True})

    return render(request, "forget_password_email.html")


def resetpassword(request):

    emailid = request.session["emailid"]
    request.session['Authentication'] = True
    data = user_info.objects.get(email=emailid)

    if request.method == "POST":

        emailid = request.session["emailid"]

        data = user_info.objects.get(email=emailid)

        otpvalue = request.POST["otp"]
        n_p_v = request.POST["newpassword"]
        c_p_v = request.POST["confirmpassword"]

        dbotp = data.otp
        print(emailid,"otptest", otpvalue)
        if otpvalue != "":

            if dbotp == otpvalue:

                return render(request, "reset_password.html", {'updatepassword': True})
            else:
                return render(request, "reset_password.html", {'OTP': True, 'wrongotp': True})

        if n_p_v != "" and c_p_v != "":
            result = confirmation(n_p_v, c_p_v, emailid)

            if result == True:

                return HttpResponse(" <h1> Password is sucessfuly updated </h1> ")

            else:
                return HttpResponse(" <h1> Password is not updated , your confirm password is wrong </h1> ")

    else:
        value1 = data.first_name
        value2 = data.last_name
        value3 = "%s %s" % (value1, value2)
        otp_msg = otp_sending()
        otp_time = time_gen()
        update = user_info(
            email=emailid,
            otp=otp_msg,
            otp_gen_time=otp_time
        )
        update.save(update_fields=["otp", "otp_gen_time"])

        smtp2(value3, otp_msg, otp_time, emailid)

    return render(request, "reset_password.html", {'otp': True})


def confirmation(np, cp, un):

        n_p_v = np
        c_p_v = cp

        if n_p_v == c_p_v:
            update = user_info(
                    email=un,
                    password=make_password(c_p_v)
                )
            update.save(update_fields=["password"])

            return True
        else:
            return False
def admin_index(request):
    try:
        auth = autherize(request.session['Authentication'],
                     request.session['role'], 2)
    except:
        return redirect("/user/login")

    if auth == True:
        return render(request, "index.html")

    else:
        aut, msg = auth
        if msg == "wrongUser":

            #return HttpResponse("you are not a valid user")
            return redirect("/user/login")
        elif msg == "notLogin":
            return redirect("/user/login")
            #return HttpResponse("you are not login for access this page")

def logout(request):
    request.session['Authentication'] = False
    request.session['emailid'] = ""
    return redirect("/user/login/")

def hoteldisplaypage(request):
    return render(request, "hoteldisplaypage.html")
