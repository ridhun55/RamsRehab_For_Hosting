from django.contrib import admin
from django.urls import path
from AdministrationApp.views import ErrorSubmit, DashboardView
from AdministrationApp.views import PatentRegistrationView, PatentTableView, PatentEditView, PatentDeleteView
from AdministrationApp.views import QuickAppointmentTableView, QuickAppointmentEditView, QuickAppointmentDeleteView
from AdministrationApp.views import AppointmentTableView, AppointmentEditView, AppointmentDeleteView
from AdministrationApp.views import TodayTableView, TomorrowTableView
from AdministrationApp.views import NurseRegisterView, DeleteNurseView
from AdministrationApp.views import AdministrationLoginView
from AdministrationApp.views import AddGalleryImage, DeleteGalleryImage
from AdministrationApp.views import AddFeedbackView, DeleteFeedbackView
from AdministrationApp.views import AddDoctorsProfileView, DeleteDoctorsProfileView
from AdministrationApp.views import ShopRequestTableView, ShopRequestStatusChangeView, DeleteShopRequestView
from AdministrationApp.views import MessageTableView, DeleteMessageView
from AdministrationApp.views import SubscribersTableView, DeleteSubscribersView
from AdministrationApp.views import AddShopItemView, DeleteShopItemView
from AdministrationApp.views import SearchPatientTableView
from AdministrationApp.views import SearchAppointmentTableView
from AdministrationApp.views import SearchQuickAppointmentTableView
from AdministrationApp.views import AddCountView, DeleteCountView
from AdministrationApp.views import AddGoogleMeetView, DeleteGoogleMeetView
from AdministrationApp.views import AddTodoView, EditTodoView, EditTodoStatusView, DeleteTodoView
from AdministrationApp.views import AddNotesView, DeleteNotesView
from AdministrationApp.views import AddAccountView, file_load_view, DeleteAccountView, DeleteAllAccountWarnningView, DeleteAllAccountView
from AdministrationApp.views import AddSocialMediaView, DeleteSocialMediaView

urlpatterns = [
    path('login/', AdministrationLoginView, name='administration_login'),
    path('error/',ErrorSubmit, name='error_submit'),
    path('', DashboardView, name='administration_home'),
    
    path('patent_registration/', PatentRegistrationView, name='patent_registration'),
    path('patents/', PatentTableView, name='patent_table'),
    path('patent/<int:id>/edit/', PatentEditView, name='patent_edit'),
    path('patent/<int:id>/delete/', PatentDeleteView, name='patent_delete'),

    path('quick_appointment/', QuickAppointmentTableView, name='quick_appointment_table'),
    path('quick_appointment/<int:id>/edit/', QuickAppointmentEditView, name='quick_appointment_edit'),
    path('quick_appointment/<int:id>/delete/', QuickAppointmentDeleteView, name='quick_appointment_delete'),

    path('appointment/', AppointmentTableView, name='appointment_table'),
    path('appointment/<int:id>/edit/', AppointmentEditView, name='appointment_edit'),
    path('appointment/<int:id>/delete/', AppointmentDeleteView, name='appointment_delete'),

    path('shop_request/', ShopRequestTableView, name='shop_request'),
    path('update_shop_request/<int:id>', ShopRequestStatusChangeView, name='update_shop_request'),
    path('shop_request/<int:id>/delete', DeleteShopRequestView, name='delete_shop_request'),
    
    path('message/', MessageTableView, name='message_table'),
    path('message/<int:id>/delete', DeleteMessageView, name='delete_message'),

    path('subscribers/', SubscribersTableView, name='subscribers_table'),
    path('subscribers/<int:id>/delete', DeleteSubscribersView, name='delete_subscribers'),

    path('today/', TodayTableView, name='today'),
    path('tomorrow/', TomorrowTableView, name='tomorrow'),

    # path('nurse/', NurseRegisterView, name='nurse_register'),
    path('register/', NurseRegisterView.as_view(), name="nurse_register"),
    path('delete/<int:id>', DeleteNurseView, name="delete_nurse"),


    path('add_image/', AddGalleryImage.as_view(), name="add_gallery_image"),
    path('image/<int:id>/delete/', DeleteGalleryImage, name="image_delete"),
    
    path('add_feedback/', AddFeedbackView.as_view(), name="add_feedback"),
    path('feedback/<int:id>', DeleteFeedbackView, name="delete_feedback"),

    path('doctors_profile/', AddDoctorsProfileView.as_view(), name="add_doctors_profile"),
    path('doctors_profile/<int:id>/delete/', DeleteDoctorsProfileView, name="delete_doctors_profile"),

    path('add_shop/', AddShopItemView.as_view(), name="add_shop_item"),
    path('shop/<int:id>/delete', DeleteShopItemView, name="delete_shop_item"),
    
    path('search_patient', SearchPatientTableView, name="search_patient_table"),
    path('search_appointment', SearchAppointmentTableView, name="search_appointment_table"),
    path('search_quick_appointment', SearchQuickAppointmentTableView, name="search_quick_appointment_table"),
    
    path('add_count', AddCountView, name="add_count"),
    path('add_count/<int:id>/delete', DeleteCountView, name="delete_count"),
    
    path('add_google-meet', AddGoogleMeetView, name="add_google_meet"),
    path('add_google-meet/<int:id>/delete', DeleteGoogleMeetView, name="delete_google_meet"),
    
    path('add_todo', AddTodoView, name="add_todo"),
    path('edit_todo/<int:id>', EditTodoView, name="edit_todo"),
    path('todo_status_change/<int:id>', EditTodoStatusView, name="todo_status_change"),
    path('todo_delete/<int:id>/delete', DeleteTodoView, name="todo_delete"),
    
    path('add_notes', AddNotesView, name="add_notes"),
    path('delete_notes/<int:id>/delete', DeleteNotesView, name="delete_notes"),
    
    path('add_account', AddAccountView, name="add_account"),
    path('export/csv/$', file_load_view, name="export_data"),
    path('delete_account/<int:id>', DeleteAccountView, name="delete_account"),
    path('delete_all_account_warnning', DeleteAllAccountWarnningView, name="delete_all_account_warnning"),
    path('delete_all_account', DeleteAllAccountView, name="delete_all_account"),
    
    path('add_social_media', AddSocialMediaView, name="add_social_media"),
    path('delete_social_media<int:id>', DeleteSocialMediaView, name="delete_social_media"),
]