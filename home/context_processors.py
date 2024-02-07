from home.models import *
# def navbar_data(request):
 
#     user_cart = Cart.objects.get(user = request.user)
#     cart_items = user_cart.cartitem_set.all()
#     total_items = cart_items.count()
#     return {'total_cart_items':total_items}



def navbar_data(request):
    total_items = 0
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        try:
            # Retrieve the user's cart and count its items
            user_cart = Cart.objects.get(user=request.user)
            total_items = user_cart.cartitem_set.count()
        except Cart.DoesNotExist:
            # Handle the case where the user doesn't have a cart
            total_items = 0

    # Return the total number of cart items
    return {'total_cart_items': total_items}