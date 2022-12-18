from django.db import models

class PatentRegistration(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    age = models.CharField(max_length=400, null=True, blank=True)
    remark = models.CharField(max_length=1000, null=True, blank=True)
    place = models.CharField(max_length=400, null=True, blank=True)
    mobile = models.CharField(max_length=400, null=True, blank=True)
    other_contact = models.CharField(max_length=400, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name


class QuickAppointment(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    age = models.CharField(max_length=400, null=True, blank=True)
    remark = models.CharField(max_length=1000, null=True, blank=True)
    place = models.CharField(max_length=400, null=True, blank=True)
    mobile = models.CharField(max_length=400, null=True, blank=True)
    other_contact = models.CharField(max_length=400, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.mobile


class Appointment(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    age = models.CharField(max_length=400, null=True, blank=True)
    remark = models.CharField(max_length=1000, null=True, blank=True)
    place = models.CharField(max_length=400, null=True, blank=True)
    mobile = models.CharField(max_length=400, null=True, blank=True)
    other_contact = models.CharField(max_length=400, null=True, blank=True)
    booking_date = models.DateField(null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    email = models.CharField(max_length=400, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True, blank=True)
    message = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.email

# ===============================================

class Nurse(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    age = models.CharField(max_length=400, null=True, blank=True)
    place = models.CharField(max_length=400, null=True, blank=True)
    username = models.CharField(max_length=1000, null=True, blank=True)
    password = models.CharField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=400, null=True, blank=True)
    mobile1 = models.CharField(max_length=400, null=True, blank=True)
    remark = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    is_nurse = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name





# =================================================

class Gallery(models.Model):
   image_title = models.CharField(max_length=255)
   image = models.ImageField(blank=True, null=True, upload_to="gallery/")
   
   def __str__(self):
      return self.image_title 

   def get_absolute_url(self):
      return reverse('gallery')


class Feedback(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to="feedback/")
    Role = models.CharField(max_length=400, null=True, blank=True)
    snippets = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
      return self.name 


class DoctorsProfile(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to="doctors/")
    mobile = models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField(max_length=400, null=True, blank=True)
    designation = models.CharField(max_length=400, null=True, blank=True)
    snippets = models.CharField(max_length=400, null=True, blank=True)
    facebook_url = models.CharField(max_length=400, null=True, blank=True)
    instagram_url = models.CharField(max_length=400, null=True, blank=True)
    twitter_url = models.CharField(max_length=400, null=True, blank=True)
    linkedin_url = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
      return self.name 
  
  
class Shop(models.Model):
    item = models.CharField(max_length=400, null=True, blank=True)
    item_Image = models.ImageField(upload_to='shop/', blank=False, null=False) 
    price = models.CharField(max_length=400, null=True, blank=True)
    offer_price = models.CharField(max_length=400, null=True, blank=True)
    category = models.CharField(max_length=400, null=True, blank=True)
    discription = models.CharField(max_length=1000, null=True, blank=True)
    rating = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.item 
  
  
class ShopRequest(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    mobile = models.CharField(max_length=400, null=True, blank=True)
    product_id = models.CharField(max_length=400, null=True, blank=True)
    price = models.CharField(max_length=400, null=True, blank=True)
    offer_price = models.CharField(max_length=400, null=True, blank=True)
    shop_status = models.CharField(max_length=400, null=True, blank=True)
    request_date = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False,null=True,blank=True)
    is_delivered = models.BooleanField(default=False,null=True,blank=True)
    

    def __str__(self):
      return self.name 
  
  
class CounterValues(models.Model):
    docter_count = models.CharField(max_length=400, null=True, blank=True)
    department_count = models.CharField(max_length=400, null=True, blank=True)
    reserchlab_count = models.CharField(max_length=400, null=True, blank=True)
    awards_count = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.docter_count


class SocialMedia(models.Model):
    twitter = models.CharField(max_length=400, null=True, blank=True)
    facebook = models.CharField(max_length=400, null=True, blank=True)
    instagram = models.CharField(max_length=400, null=True, blank=True)
    google_plus = models.CharField(max_length=400, null=True, blank=True)
    linkedin = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.facebook
  
  
class GoogleMeet(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    link = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.name

class Todo(models.Model):
    todo_name = models.CharField(max_length=400, null=True, blank=True)
    todo_dead_time = models.CharField(max_length=400, null=True, blank=True)
    todo_subject = models.CharField(max_length=400, null=True, blank=True)
    todo_body = models.CharField(max_length=400, null=True, blank=True)
    todo_status = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.todo_name

class Notes(models.Model):
    note_body = models.CharField(max_length=400, null=True, blank=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return self.note_body
  
  
class Accounts(models.Model):
    income = models.FloatField(null=True,blank=True,default=0)
    expense = models.FloatField(null=True,blank=True,default=0)
    total_expense = models.FloatField(null=True,blank=True,default=0)
    total_income = models.FloatField(null=True,blank=True,default=0)
    description = models.CharField(max_length=1000, null=True, blank=True)
    start_Date = models.DateField(null=True,blank=True)
    end_Date = models.DateField(null=True,blank=True)    
    expense_flag = models.BooleanField(default=False,null=True,blank=True)
    income_flag = models.BooleanField(default=False,null=True,blank=True)
    
    def __str__(self):
      return self.description