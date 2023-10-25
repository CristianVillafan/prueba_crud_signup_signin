from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .form import CreateOrder
from .models import Orders
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(requets):
    return render(requets, 'home.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecta'
            })
        else:
            login(request, user)
            orders=Orders.objects.filter(user=request.user)
            return render(request, 'orders.html',{
                'orders': orders
            })
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('orders')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
            })
@login_required
def signout(request):
    logout(request)
    return redirect('home')
@login_required
def orders(request):
    orders=Orders.objects.filter(user=request.user)
    return render(request, 'orders.html', {
        'orders': orders
    })
@login_required
def order_edit(request, id):
    if request.method == 'GET':
        order=get_object_or_404(Orders, pk=id, user=request.user)
        form=CreateOrder(instance=order)
        return render(request, 'order.html', {
        'order': order,
        'form': form
    })
    else:
        try:
            order=get_object_or_404(Orders, pk=id, user=request.user)
            form=CreateOrder(request.POST, instance=order)
            form.save()
            return redirect('order_detail', order.id)
        except:
            return render(request, 'order.html', {
                'order': order,
                'form': form,
                'error': "Dato invalido"
            })

@login_required
def order_detail(request, id):
    order = get_object_or_404(Orders, pk=id, user=request.user)
    return render(request, 'order_detail.html',{
        'order': order,
    })
@login_required
def order_delete(request, id):
    order=get_object_or_404(Orders, pk=id, user=request.user)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')
def whoarewe(request):
    return render(request, 'whoarewe.html')
@login_required
def create_order(request):
    if request.method == 'GET':
        return render(request, 'create_order.html', {
            'form': CreateOrder
        })
    else:
        try:
            form = CreateOrder(request.POST)
            new_order=form.save(commit=False)
            new_order.user = request.user
            new_order.save()
            return redirect('orders')
        except ValueError:
            return render(request, 'create_order.html', {
                'form': CreateOrder,
                'error': 'Por favor provee datos validos'
            })
def printing_course(request):
    return render(request, 'printing_course.html')

def maintenance_course(request):
    return render(request, 'maintenance_course.html')
