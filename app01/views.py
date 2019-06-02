from django.shortcuts import render, redirect
from app01 import models
from  django.contrib import auth
import json

from django.http import JsonResponse
# Create your views here.
def login(request):
    if request.method=="POST":
        user =  request.POST.get('user')
        pwd = request.POST.get("pwd")
        user_obj = auth.authenticate(username=user, password = pwd)
        if user_obj:
            auth.login(request,user_obj)
            return  redirect('/index/')

    return render(request,"login.html")


def index(request):
    print(request.user, type(request.user))
    time_list = models.Book.time_choices
    room_list = models.Room.objects.all()
    books =  models.Book.objects.all()
    htmls = ''
    for room in  room_list:
        htmls+="<tr><td>{}({})</td>".format(room.caption,room.num)
        for i in time_list:
            # htmls+="<td>qq</td>"
            flag =  False
            for book in books:
                if book.room == room and book.time_id == i[0]:

                    flag = True
                    break
            if flag:

                if request.user.username == book.user.username:
                    htmls += "<td class='my_ordering item' room_id ={}  time_id= {}>{}</td>".format(room.pk, i[0],
                                                                                       book.user.username)
                else:
                    htmls+="<td class='ordering item' room_id ={} time_id= {} >{}</td>".format(room.pk,i[0],book.user.username)
            else:
                htmls+="<td class='other item' room_id ={} time_id= {}></td> ".format(room.pk,i[0])

    return render(request,"index.html",locals())


