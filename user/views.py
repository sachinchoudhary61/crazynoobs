from django.shortcuts import render, HttpResponse, redirect
from user.form import user_info_form
from user.models import user_info
from django.core.files.storage import FileSystemStorage
from miscellaneous.otp_sending import otp_sending, time_gen
from miscellaneous.smtp import smtp
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

        f.image = user_image
        f.roleid_id = 2
        f.first_name = request.POST["first_name"]  # column name
        f.last_name = request.POST["last_name"]
        f.email = request.POST["email"]
        f.password = make_password(request.POST["confirm_password"])
        f.mobile_no = request.POST["mobile_no"]
        #f.address = request.POST["address"]
        f.otp = otp_sending()  # column name
        f.otp_time_gen = time_gen()
        time = "%s%s" % (time_gen())
        token = f.otp+time
        x = "%s %s" % (f.first_name, f.last_name)
        link = 'http://127.0.0.1:8000/user/activeuser/?token='+str(token)+'&email='+request.POST["email"]

        f.token = token

        f.save()
        smtp(x, link, f.otp_time_gen, f.email)

        return HttpResponse("<h1> VERIFY THE USER , SEE YOUR EMAIL </h1>")
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
        dp ="sachu"
        active = data.isactive
        if (active == False):
            return render(request, "userlogin.html", {'activeerror': True})

        else:
            if (dp == up):
                request.session['emailid'] = un
                request.session['Authentication'] = True
                return redirect("/user/signup/")
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



def updatepassword(request):


    if request.method == "POST":
        un = request.POST["email"]
        n_p_v = request.POST["newpassword"]
        c_p_v = request.POST["confirmpassword"]
        otpvalue=request.POST[""]

        data = user_info.objects.get(email=un)
        dbotp = data.otp

        if un == data.email:

            value1 = data.first_name

            value2 = data.last_name
            value3 = "%s %s" % (value1, value2)
            otp_msg = otp_sending()
            otp_time = time_gen()
            update = user_info(
                    email="stheartsachu@gmail.com",
                    otp=otp_msg,
                    otp_gen_time=otp_time
                )
            update.save(update_fields=["otp", "otp_gen_time"])

            smtp(value3, otp_msg, otp_time, un)

            return render(request, "f_pd_otp_up_pg.html", {'otp': True})

        if otpvalue != "":
            otpvalue = request.POST["otp"]
            n_p_v = request.POST["newpassword"]
            c_p_v = request.POST["confirmpassword"]
            if dbotp == otpvalue:

                return render(request, "f_pd_otp_up_pg.html", {'updatepassword': True})
            else:
                return render(request, "f_pd_otp_up_pg.html", {'otp': True, 'wrongotp': True})

        elif n_p_v != "" and c_p_v != "":
            result = confirmation(n_p_v, c_p_v, un)

            if result == True:

                return HttpResponse(" <h1> Password is sucessfuly updated </h1> ")

            else:
                return HttpResponse(" <h1> Password is not updated , your confirm password is wrong </h1> ")


        else:
            return render(request, "f_pd_em_pg.html", {'emailerror': True})

    return render(request, "f_pd_em_pg.html")



def confirmation(np, cp, un):

        n_p_v = np
        c_p_v = cp

        if n_p_v == c_p_v:
            update = user_info(
                    email=un,
                    password=c_p_v
                )
            update.save(update_fields=["password"])

            return True
        else:
            return False
