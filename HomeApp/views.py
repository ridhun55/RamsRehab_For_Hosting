from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from AdministrationApp import models

# ==============================================================

def HomeView(request):
    data = models.DoctorsProfile.objects.all()
    feedback_data = models.Feedback.objects.all()
    
    if request.method == 'POST' and 'mobile' in request.POST:
        mobile = request.POST.get('mobile')
        flag = True
        obj = models.QuickAppointment()
        obj.mobile = mobile
        obj.submit_date = datetime.today().date()
        obj.flag = flag            
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')

    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')


    context = {
        'feedback_data':feedback_data,
        'data': data, 'home':'active',
        'about':'','services':'','gallery':'','contact':'',
        'social':models.SocialMedia.objects.all()
        }
    html = 'index.html'
    return render(request,html,context)


def AboutView(request):
    c_data = models.CounterValues.objects.all()
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
    context = {'home': '', 'about': 'active', 'services': '', 'gallery': '', 'contact': ''}
    context = {'c_data':c_data }
    context = {'social':models.SocialMedia.objects.all()}
    html = 'about.html'
    return render(request,html,context)


def ServicesView(request):
    c_data = models.CounterValues.objects.all()
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
    context = {'home': '', 'c_data':c_data, 'about': '', 'services': 'active', 'gallery': '', 'contact': ''}
    context = {'social':models.SocialMedia.objects.all()}
    html = 'services.html'
    return render(request,html,context)


def GalleryView(request):
    c_data = models.CounterValues.objects.all()
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
    img_data = models.Gallery.objects.all()
    context = {'img_data': img_data,'c_data':c_data, 'home': '', 'about': '', 'services': '', 'gallery': 'active', 'contact': ''}
    context = {'social':models.SocialMedia.objects.all()}
    html = 'gallery.html'
    return render(request,html,context)


def ShopView(request):
    data = models.Shop.objects.all()
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
    context = {'data': data, 'home': '', 'about': '', 'services': '', 'gallery': 'active', 'contact': ''}
    context = {'social':models.SocialMedia.objects.all()}
    html = 'shop.html'
    return render(request,html,context)



def ShopDetailView(request,id):
    try:
        data = models.Shop.objects.get(id=id)
    except models.Shop.DoesNotExist:
        return render(request,'404.html')
    
    # data = models.Shop.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        product_id = id
        request_date = datetime.today().date()
        obj = models.ShopRequest()
        obj.name = name
        obj.mobile = mobile
        obj.product_id = product_id
        obj.request_date = request_date
        obj.price = data.price
        obj.offer_price = data.offer_price
        obj.shop_status = "New Request"
        obj.is_read = False
        obj.is_delivered = False
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
        
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'data': data, 'home': '', 'about': '', 'services': '', 'gallery': 'active', 'contact': ''}
    context = {'social':models.SocialMedia.objects.all()}
    html = 'shop_detail.html'
    return render(request,html,context)
# ==============================================================

def ContactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        submit_date = datetime.today().date()
        obj = models.Messages()
        obj.name = name
        obj.email = email
        obj.subject = subject
        obj.message = message
        obj.submit_date = submit_date
        if message == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
    
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'home': '', 'about': '', 'services': '', 'gallery': '', 'contact': 'active'}
    context = {'social':models.SocialMedia.objects.all()}
    html = 'contact.html'
    return render(request,html,context)

# ==============================================================

def AppointmentView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        remark = request.POST.get('message')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        submit_date = datetime.today().date()
        flag = True

        obj = models.Appointment()
        obj.name = name
        obj.age = age
        obj.mobile = mobile
        obj.place = place
        obj.remark = remark
        obj.submit_date = submit_date
        obj.flag = flag
        
        if mobile == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('success')
        
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'make_an_appointment.html'
    return render(request,html,context)


# ======== MigraineView ======================================

def MigraineView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'Migraine.html'
    return render(request,html,context)

# ======== MusculoskeletalView ======================================

def MusculoskeletalView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'Musculoskeletal.html'
    return render(request,html,context)

def ElbowView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/elbow.html'
    return render(request,html,context)

def HipView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/hip.html'
    return render(request,html,context)

def AnkleView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/ankle.html'
    return render(request,html,context)

def ShoulderView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/shoulder.html'
    return render(request,html,context)

def WristView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/wrist.html'
    return render(request,html,context)

def KneeJointView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/knee_joint.html'
    return render(request,html,context)

def HeadNeckView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/head_neck.html'
    return render(request,html,context)

def LumbarSpineView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/lumbar_spine.html'
    return render(request,html,context)


# =========================================

def NeurologyView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'Neurology.html'
    return render(request,html,context)

def NeurologyNoteView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/neurology_note.html'
    return render(request,html,context)

# ==========================================

def PediatricsView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'Pediatrics.html'
    return render(request,html,context)

def PaediatricNoteView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/paediatric_note.html'
    return render(request,html,context)

def MonthlyBabyMilestoneView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    context = {'social':models.SocialMedia.objects.all()}
    html = 'notes/monthly_baby_milestone.html'
    return render(request,html,context)

# ==============================================================

def SuccessView(request):
    context = {'social':models.SocialMedia.objects.all()}
    html = 'success.html'
    return render(request,html,context)


def ErrorView(request):
    context = {'social':models.SocialMedia.objects.all()}
    html = 'error.html'
    return render(request,html,context)

def SearchProductsView(request):
    if request.method == 'POST' and 'Subscribe' in request.POST:
        email = request.POST.get('email')
        objemail = models.Subscribe()
        objemail.email = email
        objemail.submit_date = datetime.today().date()
        if email == '':
            return redirect('error')
        else:
            objemail.save()
            return redirect('success')
        
    if request.method == 'POST':
        searched = request.POST['searched']
        search_post = models.Shop.objects.filter(item__icontains=searched)
        search_category = models.Shop.objects.filter(category__icontains=searched)
        
        return render(request, 'search_products.html', {
            'searched':searched, 
            'search_post':search_post, 
            'search_category':search_category
            })
    else:    
        return render(request, 'search_products.html', {}) 