from django import forms
from . models import Menu
from django.forms import Textarea, TextInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class MenuForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields =['name','image','rating','price','review']
        widgets ={
            'name':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "id":"exampleInputName1", 
                "aria-describedby":"nameHelp",
                "style":"width: 500px;",
            }),
            'image':TextInput(attrs={
                "type":"file", 
                "class":"form-control", 
                "id":"exampleInputImage1",
                "style":"width: 500px;",
            }),
            'rating':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "id":"exampleInputRating1", 
                "aria-describedby":"ratingHelp", 
                "style":"width: 500px;",
            }),
            'price':TextInput(attrs={
                "type":"int", 
                "class":"form-control", 
                "id":"exampleInputPrice1", 
                "aria-describedby":"priceHelp",
                "style":"width: 500px;",
            }),
            'review':Textarea(attrs={
                "type":"text", 
                "class":"form-control", 
                "id":"exampleInputReview1", 
                "aria-describedby":"reviewHelp",
            }),
        }
class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={"type":"text","class":"form-control","aria-describedby":"emailHelp","placeholder":"Enter Username"}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={"type":"password","class":"form-control","id":"exampleInputPassword1","placeholder":"Password"}))