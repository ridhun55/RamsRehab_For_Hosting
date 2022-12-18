from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView 


class PasswordsChangeView(PasswordChangeView):
   form_class = PasswordChangingForm
   success_url = reverse_lazy('password_success')
   

def Password_Success(request):
   return render(request, 'registration/password_success.html', {})
   

class UserRegisterView(generic.CreateView):
   form_class = SignUpForm
   template_name = 'registration/register.html'
   success_url = reverse_lazy('login')