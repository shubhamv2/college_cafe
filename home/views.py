from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from canteen_admin.models import *
from django.db.models import Q
from django.http import Http404



# Home page view
def home(request):
    food_items = FoodItem.objects.all()
    context = {'items':food_items}
    return render(request, 'home/home.html',context)


# Menu page view
def menu(request, category_name):
    food_items = FoodItem.objects.all()
    all_categories = Category.objects.all()

    categories = []

    # code for searching items
    if request.GET.get('search-text'):
        search_query = request.GET.get('search-text')
        food_items = food_items.filter(Q(food_name__icontains=search_query) | Q(food_category__food_category__icontains = search_query))

    if category_name != 'all':
        food_items = food_items.filter(food_category__food_category__iexact = category_name)

    selected_categories = request.GET.getlist('food_category',[])
    selected_meal_type = request.GET.getlist('meal_type',[])


    if 'All' in selected_categories:
        categories = FoodItem.objects.values_list('food_category__food_category', flat=True).distinct()
        selected_categories.remove('All')

    else: 
        categories = selected_categories
    
    
    if categories:
        food_items = food_items.filter(food_category__food_category__in = categories)
    

    total_items = food_items.count()
    return render(request, 'menu/menu.html', context={"items":food_items, 'categories':all_categories,'total_items':total_items})

# About page view
def about(request):
    return render(request, 'about/about.html')

# Contact page view
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('query')

        report = Report.objects.create(
            user_name = name,
            user_email = email,
            user_phone = phone,
            message = message,
        )
        report.save()
    return render(request, 'contact/contact.html')

login_required(login_url='login')
def cartPage(request):
    if request.user.is_authenticated:
        try:
            user_cart = Cart.objects.get(user=request.user)
            cart_items = user_cart.cartitem_set.all()
            context = {'cart_items': cart_items}
        except Cart.DoesNotExist:
            user_cart = None
            cart_items = []
            context = {'cart_items': cart_items}
    else:
        user_cart = None
        cart_items = []
        context = {'cart_items': cart_items}

    return render(request, 'cart/cart.html', context)



@login_required(login_url='login')
def add_to_cart(request, item_id):
    item = get_object_or_404(FoodItem, pk=item_id)
    cart, created = Cart.objects.get_or_create(user = request.user)
    cart_item, created = CartItem.objects.get_or_create(cart = cart, food_item = item)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('menu', category_name="all")



@login_required(login_url='login')
def remove_from_cart(request, item_id):
    try:
        cart = Cart.objects.get(user = request.user)
        food_item = FoodItem.objects.get(pk = item_id)
        try:
            cart_item = CartItem.objects.get(cart = cart, food_item = food_item)
            cart_item.delete()
        except CartItem.DoesNotExist:
            raise Http404("CartItem not found.")
        return redirect('cart')
    except Cart.DoesNotExist:
        raise Http404('Cart not found')