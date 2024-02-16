from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from accounts.models import User
from .models import Category, FoodItem
from home.models import Report, Order, OrderItem
from .decorators import admin_required
# Create your views here.


@admin_required
def dashboard(request):
    totalUsers = User.objects.exclude(is_superuser=True).count()
    currentDate = date.today()
    orders = Order.objects.count()
    all_orders = Order.objects.all()
    total_amount = 0
    for order in all_orders:
        order_items = OrderItem.objects.filter(order = order)
        total_amount += sum(item.price * item.quantity for item in order_items)
    context = {'totalUsers':totalUsers, 'currentDate':currentDate, 'totalorders':orders,'totalamount':total_amount}
    return render(request, 'dashboard/dashboard.html', context)
@admin_required
def addUser(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer-name')
        customer_phone = request.POST.get('customer-phone')
        customer_email = request.POST.get('customer-email')
        customer_password = request.POST.get('customer-password')
        customer_profile = request.FILES.get('customer-profile')
        if User.objects.filter(email = customer_email).exists():
            return redirect('adduser')
        create_customer = User.objects.create(
            name = customer_name,
            email = customer_email,
            phone = customer_phone,
            profile_img = customer_profile,
        )
        create_customer.set_password(customer_password)
        create_customer.save()
        return redirect('adduser')
        
    return render(request, 'adduser/adduser.html')


@admin_required
def manageUsers(request):
    customers = User.objects.all();
    context = {"customers":customers}
    return render(request, 'manageusers/manageusers.html', context)

@admin_required
def addCategory(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        food_category = Category.objects.create(food_category = category)
        food_category.save()
        return redirect('addcategory')
    return render(request, 'addcategory/addcategory.html')


@admin_required
def manageCategories(request):
    allCategories = Category.objects.all();
    context = {'categories': allCategories}
    return render(request, 'managecategories/managecategories.html', context)

@admin_required
def addFood(reqeust):
    if reqeust.method == 'POST':
        food_name = reqeust.POST.get('foodname')
        food_price = reqeust.POST.get('foodprice')
        food_category = reqeust.POST.get('foodcategory')
        food_subcategory = reqeust.POST.get('foodsubcategory')
        food_desc = reqeust.POST.get('fooddesc')
        food_img = reqeust.FILES.get('foodimage')
        food_category_instance = Category.objects.get(food_category = food_category)
        FoodItem.objects.create(
            food_name = food_name,
            food_price = food_price,
            food_category = food_category_instance,
            food_subcategory = food_subcategory,
            food_desc = food_desc,
            food_image = food_img,
        )
    allCategories = Category.objects.all();
    context = {"categories":allCategories}    
    return render(reqeust,'addfood/addfood.html',context)
@admin_required
def manageFoods(request):
    allItems = FoodItem.objects.all();
    context = {"foodItems": allItems}
    return render(request, 'managefoods/managefoods.html',context)


@admin_required
def reports(request):
    allReports = Report.objects.all();
    context = {'reports':allReports}
    return render(request, 'reports/reports.html',context)

@admin_required
def deleteReport(request, id):
    try:
        report = Report.objects.get(pk= id);
        report.delete()
    except Exception as e:
        return redirect('reports')
    return redirect('reports')


@admin_required
def deleteUser(reqeust, id):
    user_to_delete = User.objects.get(id=id)
    user_to_delete.delete()
    return redirect('manageusers')


@admin_required
def deleteCategory(reqeust, id):
    category_to_delete = Category.objects.get(id=id)
    category_to_delete.delete()
    return redirect('managecategories')

@admin_required
def deleteFoodItem(reqeust, id):
    item_to_delete = FoodItem.objects.get(id = id)
    item_to_delete.delete()
    return redirect('managefoods')

@admin_required
def editUser(request, id):
    userInstance = User.objects.get(pk = id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer-name')
        customer_phone = request.POST.get('customer-phone')
        customer_password = request.POST.get('customer-password')
        customer_profile = request.FILES.get('customer-profile')
        if customer_name:
            userInstance.name = customer_name
        if customer_phone:
            userInstance.phone = customer_phone
        if customer_profile:
            userInstance.profile_img = customer_profile
        if customer_password:
            userInstance.set_password(customer_password)
        userInstance.save()
        return redirect('manageusers')
    context = {'userdetails':userInstance}
    return render(request, 'edituser/edituser.html',context)



@admin_required
def orders(request):
    all_orders = Order.objects.all().order_by('-created_at')
    context = {'orders':all_orders}
    return render(request, 'orders/orders.html', context)


