from django.shortcuts import render, HttpResponse, redirect

from PIL import ImageTk, Image
from django.core.files.storage import FileSystemStorage
from manager.form import hotelinfoForm, hotelroomsForm, room_typeForm, hotelroomimageForm
from manager.models import hotelroomimages, hotelrooms, hotelinfo, hotelguestinfo, room_type
from user.models import user_info

# Create your views here

def managerindex(request):

    return render(request, "managerindex.html")

def businessusermainpage(request):
    request.session['Authentication'] = True
    un = request.session['emailid']

    return render(request, "hotelindex.html")


def businessusercontactpage(request):
    return render(request, "contact.html")

def hotelinfofn(request):

    if request.method == "POST":
        hotel_image = None
        if request.FILES["image1"]:
            myfile = request.FILES["image1"]
            myfile.resize((250, 200), Image.NEAREST)
            fs = FileSystemStorage()
            filename = fs.save("hotel_image/"+myfile.name, myfile)
            hotel_image = fs.url(filename)
            hotel_image = myfile.name

        form = hotelinfoForm(request.POST)
        f = form.save(commit=False)

        f.app_id_id = 2
        un = request.session['emailid']
        f.email_id = un
        f.hotel_status = request.POST["booking"]
        f.hotel_name = request.POST["hotel_name"]
        f.hotel_city = request.POST["hotel_city"]
        f.hotel_image = hotel_image
        f.hotel_address = request.POST["hotel_address"]
        f.hotel_no_rooms = request.POST["no_of_room"]

        #f.hotel_room_price = request.POST["room_price"]

        f.hotel_helpline_no = request.POST["hotel_helpline_number"]
        f.room_with_meal_or_without_meal = request.POST["meal_service"]
        f.save()

        form1 = hotelroomsForm(request.POST)
        f1 = form1.save(commit=False)

        h_data = hotelinfo.objects.all().order_by('-hotel_id')[0:1]
        h_id = 0
        for data in h_data:
            h_id += data.hotel_id
        f1.hotel_id_id = h_id
        f1.room_occupied = 0

        f1.isactive = request.POST["booking"]
        f1.save()

        type1 = request.POST["roomtype1"]
        type2 = request.POST["roomtype2"]
        type3 = request.POST["roomtype3"]

        type1price = request.POST["roomtype1price"]
        type2price = request.POST["roomtype2price"]
        type3price = request.POST["roomtype3price"]

        room_data = hotelrooms.objects.all().order_by('-room_id')[0:1]

        room_id = 0
        for r_data in room_data:
            room_id += r_data.room_id
        #tr = 0
        roomtypelist = []
        typepricelist = []

        if type1 != "":
            #tr += 1
            roomtypelist.append(type1)
            typepricelist.append(type1price)
        if type2 != "":
            #tr += 1
            roomtypelist.append(type2)
            typepricelist.append(type2price)
        if type3 != "":
            roomtypelist.append(type3)
            typepricelist.append(type3price)
            #tr += 1

        for i, j in zip(roomtypelist, typepricelist):
            form2 = room_typeForm(request.POST)
            f2 = form2.save(commit=False)
            f2.room_type = i
            f2.room_type_price = j
            f2.room_id_id = room_id
            f2.save()

        for i in range(2, 7):

            form3 = hotelroomimageForm(request.POST)
            f3 = form3.save(commit=False)
            hotel_room_image = None
            if request.FILES["image"+str(i)]:
                myfile = request.FILES["image"+str(i)]
                myfile.resize((250, 200), Image.NEAREST)
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                hotel_room_image = fs.url(filename)
                hotel_room_image = myfile.name

            f3.image = hotel_room_image
            f3.room_id_id = room_id
            f3.isactive = 1
            f3.save()

        return render(request, "hotelindex.html")

    return render(request, "addhotelinfo.html")

def fetchinghotelinfo(request):# using get key

    un = request.session['emailid']
    h_data = hotelinfo.objects.filter(email_id=un)
    u_data = user_info.objects.filter(email=un)
    return render(request, "managehotel.html", {"hd": h_data}, {"ud": u_data})

def edithoteldata(request):

    hid = request.GET['hid']

    if request.method == "POST":
        hotel_image = None
        if request.FILES["image1"]:
            myfile = request.FILES["image1"]
            myfile.resize((250, 200), Image.NEAREST)
            fs = FileSystemStorage()
            filename = fs.save("hotel_image/" + myfile.name, myfile)
            hotel_image = fs.url(filename)
            hotel_image = myfile.name

        status = request.POST["booking"]
        name = request.POST["hotel_name"]
        city = request.POST["hotel_city"]
        image = hotel_image
        address = request.POST["hotel_address"]
        # f.hotel_room_price = request.POST["room_price"]
        helpline_no = request.POST["hotel_helpline_number"]
        meal_services = request.POST["meal_service"]

        update = hotelinfo(

            hotel_id=hid,
            hotel_status=status,
            hotel_name=name,
            hotel_city=city,
            hotel_image=image,
            hotel_address=address,
            hotel_helpline_no=helpline_no,
            room_with_meal_or_without_meal=meal_services,

        )
        update.save(update_fields=["hotel_status", "hotel_name", "hotel_city",
                                       "hotel_image", "hotel_address", "hotel_helpline_no",
                                       "room_with_meal_or_without_meal"])

        return redirect("/manager/fetchinghotelinfo/")

    return render(request, "edithotelprofile.html")

# def hotelroomprice(request):
#     for i in range(2, 7):
#
#
#         hotel_room_image = None
#         if request.FILES["image" + str(i)]:
#             myfile = request.FILES["image" + str(i)]
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             hotel_room_image = fs.url(filename)
#             hotel_room_image = myfile.name
#
#         h_r_image = hotel_room_image
#
#         update = hotelroomimages(
#
#             image=h_r_image,
#         )
#         update.save(update_fields=["image"])
#     type1 = request.POST["roomtype1"]
#     type2 = request.POST["roomtype2"]
#     type3 = request.POST["roomtype3"]
#
#     type1price = request.POST["roomtype1price"]
#     type2price = request.POST["roomtype2price"]
#     type3price = request.POST["roomtype3price"]
#
#     tr = 0
#     roomtypelist = []
#     typepricelist = []
#     if type1 != "":
#         tr += 1
#         roomtypelist.append(type1)
#         typepricelist.append(type1price)
#     if type2 != "":
#         tr += 1
#         roomtypelist.append(type2)
#         typepricelist.append(type2price)
#     if type3 != "":
#         roomtypelist.append(type3)
#         typepricelist.append(type3price)
#         tr += 1
#
#     for i, j in zip(roomtypelist, typepricelist):
#         update = room_type(
#             room_type=i,
#             room_type_price=j,
#         )
#         update.save(update_fields=["room_type", "room_type_price"])
#
# room_number = request.POST["no_of_room"]
# room_activeness = request.POST["booking"]
#
# update = hotelrooms(
#     hotel_id_id=hid,
#     room_no=room_number,
#     isactive=room_activeness,
# )
# update.save(update_fields=["room_no", "isactive"])