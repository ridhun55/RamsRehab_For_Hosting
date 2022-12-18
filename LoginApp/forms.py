from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class SignUpForm(UserCreationForm):
   email = forms.EmailField(required = False, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Id'}))
   first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name *'}))
   last_name = forms.CharField(max_length=100,required = False, widget=forms.TextInput(attrs={'class':' form-control','placeholder':'Enter Last Name'}))
   is_staff = forms.BooleanField(required = False, widget=forms.CheckboxInput(attrs={'class':'form-check form-check-inline'}))

   class Meta:
      model = User
      fields = ('first_name', 'last_name', 'email','username' , 'password1', 'password2','is_staff' )


   def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)
      
      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'Enter UserName *'
      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password *'
      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placeholder'] = 'Enter Password Again *'
      

class PasswordChangingForm(PasswordChangeForm):
   old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password','placeholder':'Enter Old Password'}))
   new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password','placeholder':'Enter New Password'}))
   new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password','placeholder':'Enter Confirm Password'}))
   
   class Meta:
      model = User
      fields = ('old_password', 'new_password1', 'new_password2')