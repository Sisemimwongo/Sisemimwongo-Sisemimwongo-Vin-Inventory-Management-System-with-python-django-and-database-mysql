from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    products_count = products.count()
    workers_count = User.objects.all().count()
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': order,
        'form': form,
        'products': product,
        'products_count': products_count,
        'workers_count': workers_count,
        'order_count': orders_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    product = Product.objects.all()
    product_count = product.count()
    orders = Order.objects.all()
    orders_count = orders.count()

    context = {
        'workers': workers,
        'workers_count': workers.count,
        'product_count': product_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def product(request):
    items = Product.objects.all() # using ORM
    items = Product.objects.raw('SELECT * FROM dashboard_product')
    product = Product.objects.all()
    product_count = product.count()
    orders = Order.objects.all()
    orders_count = orders.count()
    workers = User.objects.all()
    workers_count = workers.count()
    if request.method =='POST':
        form = ProductForm()
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product} has been added' )
            return redirect('dahboard-product')
    context = {
        'items': items,
        'product_count': product_count,
        'orders_count': orders_count,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', {'form': form})

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    product = Product.objects.all()
    product_count = product.count()
    workers = User.objects.all()
    workers_count = workers.count()

    context = {
        'orders': orders,
        'orders_count': orders_count,
        'product_count': product_count,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/order.html', context)

def user_logout(request):
    logout(request)
    return redirect('user-login')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new product
            return redirect('success_url')  # Redirect to a success page or another view
    else:
        form = ProductForm()  # Create a new empty form

    return render(request, 'add_product.html', {'form': form})


