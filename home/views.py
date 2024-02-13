from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from canteen_admin.models import *
from django.db.models import Q
from django.http import Http404
from django.contrib import messages




# Home page view
def home(request):
    food_items = FoodItem.objects.all()
    reviews = Review.objects.all()
  
    context = {'items':food_items, 'reviews':reviews}
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

        if not all([name, phone, email,message]):
            messages.error(request, 'All fields are required')
            return redirect('contact')


        report = Report.objects.create(
            user_name = name,
            user_email = email,
            user_phone = phone,
            message = message,
        )
        report.save()
        
    return render(request, 'contact/contact.html')



# Home page review
@login_required(login_url='login')
def review_page(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            review = request.POST.get('review')
            user = request.user
            Review.objects.create(
                user = user,
                review = review,
            )
            
    return redirect('home')


# Cart Page View
@login_required(login_url='login')
def cartPage(request):
    if request.user.is_authenticated:
        try:
            total_amount = 0
            user_cart = Cart.objects.get(user=request.user)
            cart_items = user_cart.cartitem_set.all()
            for cart_item in cart_items:
                total_amount += (cart_item.quantity * cart_item.food_item.food_price)
            context = {'cart_items': cart_items, 'total_amount':total_amount}
        except Cart.DoesNotExist:
            user_cart = None
            cart_items = []
            context = {'cart_items': cart_items}
    else:
        user_cart = None
        cart_items = []
        context = {'cart_items': cart_items}

    return render(request, 'cart/cart.html', context)


# Users Orders
@login_required(login_url='login')
def userOrders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user = request.user).order_by('-created_at')
        total_amount = 0
        for order in orders:
            items = OrderItem.objects.filter(order = order)
            for item in items:
                total_amount +=( (item.quantity) * (item.food_item.food_price))
        context ={'orders': orders, 'total_amount':total_amount}

    return render(request, 'userorders/userorders.html',context)



# Logic for canceling order
@login_required(login_url='login')
def cancelOrder(request, order_id, item_id):
    if request.user.is_authenticated:
        order_item = get_object_or_404(OrderItem, id=item_id, order__id = order_id)
        if order_item.order.user != request.user:
            return HttpResponse('Access denied')
        order = Order.objects.get(user = request.user, pk = order_id)
        order_item = OrderItem.objects.get(order=order, pk=item_id)
        order_cancel_price = order_item.price * order_item.quantity
        order.total_price -= order_cancel_price
        order.save()
        order_item.delete()

        return redirect('userorders')
    else:
        return HttpResponse('Bad Request !')




# Logic for adding item into cart
@login_required(login_url='login')
def add_to_cart(request, item_id):

    item = get_object_or_404(FoodItem, pk=item_id)
    
    # Ensure the user is authenticated
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, food_item=item)
        cart_item.quantity += 1
        # cart_item.save()
    
    return redirect('menu', category_name="all")





    


# Logic for removing item from cart
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

# Logic for incrementing item into cart
@login_required(login_url='home')
def increment_item(request, item_id):
    try:
        cart = Cart.objects.get(user = request.user)
        food_item = FoodItem.objects.get(pk = item_id)
        try:
            cart_item = CartItem.objects.get(cart = cart, food_item = food_item)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            raise Http404("CartItem not found.")
        return redirect('cart')
    except Cart.DoesNotExist:
        raise Http404('Cart not found')
    

#logic for decrementing item from cart
@login_required(login_url='home')
def decrement_item(request, item_id):
    try:
        cart = Cart.objects.get(user = request.user)
        food_item = FoodItem.objects.get(pk = item_id)
        try:
            cart_item = CartItem.objects.get(cart = cart, food_item = food_item)
            if(cart_item.quantity > 1):
                cart_item.quantity -= 1
            
            cart_item.save()
        except CartItem.DoesNotExist:
            raise Http404("CartItem not found.")
        return redirect('cart')
    except Cart.DoesNotExist:
        raise Http404('Cart not found')
    

# Logic for placing order
@login_required(login_url='login')
def place_order(request):
    if request.user.is_authenticated:
            total_amount = 0
            user_cart = Cart.objects.get(user=request.user)
            cart_items = user_cart.cartitem_set.all()

            for cart_item in cart_items:
                total_amount += (cart_item.quantity * cart_item.food_item.food_price)

            if request.method == 'POST':
                user = request.user
                total_price = total_amount
                first_name = request.POST.get('first-name')
                last_name = request.POST.get('last-name')
                address = request.POST.get('address')
                city = request.POST.get('city')
                state = request.POST.get('state')
                pin = request.POST.get('pin')
                phone = request.POST.get('phone')
                payment_option = request.POST.get('payment')
                if not all([first_name, last_name, address, city, state, pin, phone]):
                    messages.error(request, 'All fields are required')
                    return redirect('cart')
                
               

                
                if payment_option == 'online':
                    request.session['total_price'] = str(total_price)
                    request.session['first_name'] = first_name
                    request.session['last_name'] = last_name
                    request.session['city_name'] = city
                    request.session['state_name'] = state
                    request.session['pin_code'] = pin
                    request.session['phone_number'] = phone
                    request.session['address'] = address
                    return redirect('paymentpage')
                
                elif payment_option == 'cash':

                    order = Order.objects.create(
                    user = user,
                    total_price = total_price,
                    first_name = first_name,
                    last_name = last_name,
                    city_name = city,
                    state_name = state,
                    pin_code = pin,
                    phone_number = phone,
                    address = address
                    )
                    order.save()

                    for cart_item in cart_items:
                        quantity = cart_item.quantity
                        item_id = cart_item.food_item.id
                        item = FoodItem.objects.get(pk = item_id)
                        price = item.food_price
                        OrderItem.objects.create(order = order, food_item = item, quantity = quantity, price  = price)

                    Cart.objects.filter(user = request.user).delete()
                    return redirect('ordersuccess')
    return redirect('cart')

# Login for payment Fake payment
@login_required(login_url='login')
def makePayment(request):
    user = request.user
    user_cart = Cart.objects.get(user=request.user)
    cart_items = user_cart.cartitem_set.all()
    total_price = request.session.get('total_price')
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    city_name = request.session.get('city_name')
    state_name = request.session.get('state_name')
    pin_code = request.session.get('pin_code')
    phone_number = request.session.get('phone_number')
    address = request.session.get('address')
    total_price = float(total_price)

    order = Order.objects.create(
        user = user,
        total_price = total_price,
        first_name = first_name,
        last_name = last_name,
        city_name = city_name,
        state_name = state_name,
        pin_code = pin_code,
        phone_number = phone_number,
        is_paid = True,
        address = address,
    )
    order.save()

    for cart_item in cart_items:
        quantity = cart_item.quantity
        item_id = cart_item.food_item.id
        item = FoodItem.objects.get(pk = item_id)
        price = item.food_price
        OrderItem.objects.create(order = order, food_item = item, quantity = quantity, price  = price)
    Cart.objects.filter(user = request.user).delete()
    return redirect('ordersuccess')



# Login to show success page after order succesfully placed 
@login_required(login_url='login')
def order_success(request):
    return render(request, 'success/success.html')

# Login for showing payament card during placing order
@login_required(login_url='login')
def payment(request):
    total_price = request.session.get('total_price')
    total_price = float(total_price)  
    context = {'total_amount': total_price}
    return render(request, 'payment/payment.html', context)


