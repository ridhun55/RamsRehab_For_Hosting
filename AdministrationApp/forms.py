from django import forms
from django.db import models
from django.forms import widgets
from AdministrationApp.models import Gallery, DoctorsProfile, Feedback, Shop

class GalleryForm(forms.ModelForm):
   class Meta:
      model = Gallery
      fields = ('image_title', 'image')
      
      widgets = {
         'image_title': forms.TextInput(attrs={'class':'form-control','placeholder':'example : Rams Rehab Lab Facilities'}),
      }

class FeedbackForm(forms.ModelForm):
   class Meta:
      model = Feedback
      fields = ('name', 'profile_photo','Role','snippets')
      
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'Role': forms.TextInput(attrs={'class':'form-control','placeholder':'example : Doctor, Patient, etc'}),
         'snippets': forms.TextInput(attrs={'class':'form-control','placeholder':'max 31 words, min 29 words'}),
      }



class DoctorsForm(forms.ModelForm):
   class Meta:
      model = DoctorsProfile
      fields = ('name', 'profile_photo', 'mobile','email','designation','snippets','facebook_url','instagram_url','twitter_url','linkedin_url')
      
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'email': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'designation': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'snippets': forms.TextInput(attrs={'class':'form-control','placeholder':'max 10 words, min 8 words'}),
         'facebook_url': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'instagram_url': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'twitter_url': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'linkedin_url': forms.TextInput(attrs={'class':'form-control','placeholder':''})
      }


class ShopForm(forms.ModelForm):
   class Meta:
      model = Shop
      fields = ('item', 'price','offer_price','category', 'item_Image','discription')
      
      widgets = {
         'item': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'price': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'offer_price': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'category': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
         'discription': forms.Textarea(attrs={'class':'form-control','placeholder':'About Product discriptions.. '}),
         'rating': forms.TextInput(attrs={'class':'form-control','placeholder':''}),  
      }