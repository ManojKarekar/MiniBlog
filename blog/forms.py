from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy as _
from .models import post

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        labels = {
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
        }

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }


class Login(AuthenticationForm):
    username = UsernameField(widget= forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False,widget= forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



class postForm(forms.ModelForm):
    class Meta:
        model = post   
        fields = ['title','desc']
        labels = {"title":'Title of the Post   ', "desc":"Description of the Post  "}
        widgets = {
          "title": forms.TextInput(attrs={"class":"form-control"}),
          "desc": forms.Textarea(attrs={"class":"form-control"})
        }