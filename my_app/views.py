from django.shortcuts import render,redirect
from.models import User_table, Products_table, Cart_table

# Create your views here.
def home(request):
    products = Products_table.objects.all()
    if products:
        return render(request, 'home.html',{'data':products})
    else:
        return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES['image']
        product = Products_table(name=name, price=price, description=description, image=image)
        product.save()
        return redirect('/home')
    return render(request, 'add_product.html')

# def delete_product(request, id):
#     product = Products_table.objects.get(id=id)
#     product.delete()
#     return redirect('/home')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User_table.objects.filter(email=email):
            error = 'Email already exists'
            return render(request, 'register.html', {'error': error})
        else:
            user = User_table(name=name, email=email, password=password)
            user.save()
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User_table.objects.get(email=email, password=password)
        print(user)
        if user:
            request.session['user_id'] = user.id
            return redirect('/home')
        else:
            error = 'Invalid credentials'
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def add_to_cart(request, pid):
    if 'user_id' in request.session:
        product_id = Products_table.objects.get(id=pid)
        user_id = User_table.objects.get(id=request.session['user_id'])
        if Cart_table.objects.filter(product_id = product_id, user_id=user_id):
            cart_obj = Cart_table.objects.get(product_id = product_id, user_id=user_id)
            cart_obj.quantity += 1
            cart_obj.save()
            return redirect('/home')
        else:
            cart_obj = Cart_table(
                user_id = user_id,
                product_id = product_id,
                quantity = 1
            )
            cart_obj.save()
            return redirect('/home')
    else:
        return redirect('/')

def remove_from_cart(request, id):
    if 'user_id' in request.session:
        cart_obj = Cart_table.objects.get(id=id)
        cart_obj.delete()
        return redirect('/view_cart')
    else:
        return redirect('/')

def update_cart(request, id):
    if 'user_id' in request.session:
        cart_obj = Cart_table.objects.get(id=id)
        if request.method == 'POST':
            cart_obj.quantity = request.POST['quantity']
            cart_obj.save()
            return redirect('/view_cart')
    else:
        return redirect('/')

def view_cart(request):
    if 'user_id' in request.session:
        cart_obj = Cart_table.objects.filter(user_id=request.session['user_id'])
        # total = 0
        # for item in cart_obj:
        #     total += item.product_id.price * item.quantity
        return render(request, 'view_cart.html', {'data': cart_obj})
    else:
        return redirect('/')

def checkout(request):
    if 'user_id' in request.session:
        cart_obj = Cart_table.objects.filter(user_id=request.session['user_id'])
        total = 0
        for item in cart_obj:
            total += item.product_id.price * item.quantity
        return render(request, 'checkout.html', {'data': cart_obj, 'total': total})
    else:
        return redirect('/')