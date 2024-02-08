from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from accounts.models import User
from .models import Category, FoodItem
from home.models import Report
# Create your views here.

def dashboard(request):
    totalUsers = User.objects.exclude(is_superuser=True).count()
    currentDate = date.today()
    context = {'totalUsers':totalUsers, 'currentDate':currentDate}
    return render(request, 'dashboard/dashboard.html', context)

def addUser(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer-name')
        customer_phone = request.POST.get('customer-phone')
        customer_email = request.POST.get('customer-email')
        customer_password = request.POST.get('customer-email')
        customer_profile = request.POST.get('customer-profile')
        if User.objects.filter(email = customer_email).exists():
            return redirect('adduser')
        create_customer = User.objects.create(
            name = customer_name,
            email = customer_email,
            phone = customer_phone,
            profile_img = customer_profile,
        )
        create_customer.check_password(customer_password)
        create_customer.save()
        return redirect('adduser')
        
    return render(request, 'adduser/adduser.html')



def manageUsers(request):
    customers = User.objects.all();
    context = {"customers":customers}
    return render(request, 'manageusers/manageusers.html', context)


def addCategory(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        food_category = Category.objects.create(food_category = category)
        food_category.save()
        return redirect('addcategory')
    return render(request, 'addcategory/addcategory.html')



def manageCategories(request):
    allCategories = Category.objects.all();
    context = {'categories': allCategories}
    return render(request, 'managecategories/managecategories.html', context)


def addFood(reqeust):
    if reqeust.method == 'POST':
        food_name = reqeust.POST.get('foodname')
        food_price = reqeust.POST.get('foodprice')
        food_category = reqeust.POST.get('foodcategory')
        food_desc = reqeust.POST.get('fooddesc')
        food_img = reqeust.FILES.get('foodimage')
        food_category_instance = Category.objects.get(food_category = food_category)
        FoodItem.objects.create(
            food_name = food_name,
            food_price = food_price,
            food_category = food_category_instance,
            food_desc = food_desc,
            food_image = food_img,
        )
    allCategories = Category.objects.all();
    context = {"categories":allCategories}    
    return render(reqeust,'addfood/addfood.html',context)

def manageFoods(request):
    allItems = FoodItem.objects.all();
    context = {"foodItems": allItems}
    return render(request, 'managefoods/managefoods.html',context)



def reports(request):
    allReports = Report.objects.all();
    context = {'reports':allReports}
    return render(request, 'reports/reports.html',context)



def deleteUser(reqeust, id):
    user_to_delete = User.objects.get(id=id)
    user_to_delete.delete()
    return redirect('manageusers')



def deleteCategory(reqeust, id):
    category_to_delete = Category.objects.get(id=id)
    category_to_delete.delete()
    return redirect('managecategories')


def deleteFoodItem(reqeust, id):
    item_to_delete = FoodItem.objects.get(id = id)
    item_to_delete.delete()
    return redirect('managefoods')


def editUser(reqeust, id):
    userInstance = get_object_or_404(User, pk = id)
    if reqeust.method == 'POST':
        pass
    context = {'userdetails':userInstance}
    return render(reqeust, 'edituser/edituser.html',context)