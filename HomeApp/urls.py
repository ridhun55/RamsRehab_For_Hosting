from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('services/', views.ServicesView, name='services'),
    path('gallery/', views.GalleryView, name='gallery'),
    path('shop/', views.ShopView, name='shop'),
    path('shop/<int:id>', views.ShopDetailView, name='shop_detail'),
    
    path('contact/', views.ContactView, name='contact'),
    path('appointment/', views.AppointmentView, name='appointment'),

    path('migraine/', views.MigraineView, name='migraine'),
    
    path('musculoskeletal/', views.MusculoskeletalView, name='musculoskeletal'),
    path('musculoskeletal/elbow', views.ElbowView, name='elbow'),
    path('musculoskeletal/hip', views.HipView, name='hip'),
    path('musculoskeletal/ankle', views.AnkleView, name='ankle'),
    path('musculoskeletal/shoulder', views.ShoulderView, name='shoulder'),
    path('musculoskeletal/wrist', views.WristView, name='wrist'),
    path('musculoskeletal/knee_joint', views.KneeJointView, name='knee_joint'),
    path('musculoskeletal/head_neck', views.HeadNeckView, name='head_neck'),
    path('musculoskeletal/lumbar_spine', views.LumbarSpineView, name='lumbar_spine'),

    path('neurology/', views.NeurologyView, name='neurology'),
    path('neurology/neurology_note', views.NeurologyNoteView, name='neurology_note'),
    
    path('pediatrics/', views.PediatricsView, name='pediatrics'),
    path('paediatric/paediatric_note', views.PaediatricNoteView, name='paediatric_note'),
    path('paediatric/monthly_baby_milestone', views.MonthlyBabyMilestoneView, name='monthly_baby_milestone'),

    path('success/', views.SuccessView, name='success'),
    path('error/', views.ErrorView, name='error'),
    path('search_products/', views.SearchProductsView, name="search_products"),
]