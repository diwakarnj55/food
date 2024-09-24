from django.shortcuts import render,redirect
from . models import food, Menu, Add, itemadd
from . forms import MenuForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    bio=food.objects.all()
    data ={
        "bio":bio
    }
    return render(request, "index.html",data)
def post(request, id):
    menu=Menu.objects.all()
    dish=food.objects.get(id=id)
    data ={
        "dish":dish,
        "menu":menu,
    }
    return render(request, "post.html",data)
def menu(request):
    menu1=MenuForm()
    data ={
        "menu1":menu1,
    }
    if request.method=="POST":
        menu1=MenuForm(request.POST)
        if menu1.is_valid():
            menu1.save()
    return render(request, "menu.html",data)
def add_to_cart(request, id):
    pro=Menu.objects.get(id=id)
    cart_name, created=Add.objects.get_or_create(name=pro,user=request.user)
    cart_name.qty+=1
    cart_name.save()
    return redirect("view_cart")
def view_cart(request):
    Add_name=Add.objects.filter(user=request.user)
    total=sum(item.name.price*item.qty for item in Add_name)
    using=Add.objects.all()
    data ={
        "using":using,
        "total":total,
        "Add_name":Add_name,
    }
    return render(request, "view_cart.html",data)
def remove_cart(request,id):
    cart_name = Add.objects.get(id=id)
    cart_name.delete()
    return redirect("view_cart")
def item(request):
    menu=Menu.objects.all()
    add=itemadd.objects.all()
    Add_name=Add.objects.filter(user=request.user)
    total=sum(item.name.price*item.qty for item in Add_name)
    data ={
        "menu":menu,
        "add":add,
        "total":total,
    }
    return render(request, "itemadd.html",data)
def Atm(request):
    return render(request, "atm.html")