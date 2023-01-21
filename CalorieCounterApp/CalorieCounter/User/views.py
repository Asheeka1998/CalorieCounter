from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
# Create your views here.
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import FoodConsumption, ActivityPerformed, User, UserNewActivity, UserNewItem
from ..Admin.models import Foods, Activities


def DisplayFood(request):
    food = Foods.objects.all()
    return JsonResponse(food)


def DisplayActivity(request):
    Activity = Activities.objects.all()
    return JsonResponse(Activity)


# signup page
def RegisterPage(request):
    form = User()
    if request.method == 'POST':
        form.username = request.POST.get("username")
        form.mail_id = request.POST.get("mail_id")
        form.password = request.POST.get("password")
        form.save()
        return HttpResponse("Account was created for " + form.username)
    return HttpResponse("Method is not Post")


# login page
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user_obj = User.objects.filter(username=username, password=password)
                request.session['sessionid'] = user_obj.id
                return HttpResponse("Login Successfully")
            else:
                return HttpResponse('Username or password is incorrect')
        return HttpResponse('Please login')


# logout page
def LogOutPage(request):
    logout(request)
    return HttpResponse('User logged out')


# # for selecting food each day
@login_required
def select_food(request):
    person = User.objects.get(id=request.session['sessionid'])

    if request.method == 'POST':
        form = FoodConsumption()
        form.user_id = person
        form.selected_food = request.POST.get('select_food')
        form.today_date = request.POST.get('date')
        form.quantity_consumed = request.POST.get('select_qty')
        calories = request.POST.get('select_calorie')
        form.calorie_count = int(calories) * int(form.quantity_consumed)
        form.save()
        return HttpResponse("Saved")
    else:
        return HttpResponse("Select food")


@login_required
def select_activity(request):
    person = User.objects.get(id=request.session['sessionid'])

    if request.method == 'POST':
        form = ActivityPerformed()
        form.user_id = person
        form.selected_activity = request.POST.get('select_activity')
        form.today_date = request.POST.get('date')
        form.time_spent = request.POST.get('select_time duration')
        calories = request.POST.get('select_calorie_burn')
        form.calorie_count = int(calories) * int(form.time_spent)
        form.save()
        return HttpResponse("Saved")
    else:
        return HttpResponse("Select Activity")


@login_required
def AddActivityByUser(request):
    person = User.objects.get(id=request.session['sessionid'])
    if request.method == 'POST':
        form = UserNewActivity()
        form.user_id = person
        form.Activity_name = request.POST.get('select_activity')
        form.time_duration = request.POST.get('select_time duration')
        form.calorie_burns = request.POST.get('select_calorie')
        form.Status = 0
        form.save()
        return HttpResponse("New Activity Saved")
    else:
        return HttpResponse("Add new  Activity")


@login_required
def AddItemByUser(request):
    person = User.objects.get(id=request.session['sessionid'])
    if request.method == 'POST':
        form = UserNewItem()
        form.user_id = person
        form.Item_name = request.POST.get('select_activity')
        form.calorie = request.POST.get('select_calorie')
        form.Status = 0
        form.save()
        return HttpResponse("New Item Saved")
    else:
        return HttpResponse("Add new Item")


def ViewReports(request, date1, date2=""):
    if date2 == "":
        obj = FoodConsumption.objects.filter(today_date=date1)
        obj1 = ActivityPerformed.objects.filter(today_date=date1)
    else:
        obj = FoodConsumption.objects.filter(effected_date_range=(date1, date2))
        obj1 = ActivityPerformed.objects.filter(effected_date_range=(date1, date2))
    return JsonResponse({'ItemStatus': obj, "ActivityStatus": obj1})
