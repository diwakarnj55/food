from django.urls import path
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("post/<int:id>",views.post,name="post"),
    path("menu",views.menu,name="menu"),
    path("add_to_cart/<int:id>",views.add_to_cart,name="add_to_cart"),
    path("view_cart",views.view_cart,name="view_cart"),
    path("remove_cart/<int:id>",views.remove_cart,name="remove_cart"),
    path("itemadd/",views.item,name="itemadd"),
    path("atm",views.Atm,name="atm"),
]