# Generated by Django 3.2.16 on 2022-12-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.FloatField(blank=True, default=0, null=True)),
                ('expense', models.FloatField(blank=True, default=0, null=True)),
                ('total_expense', models.FloatField(blank=True, default=0, null=True)),
                ('total_income', models.FloatField(blank=True, default=0, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_Date', models.DateField(blank=True, null=True)),
                ('end_Date', models.DateField(blank=True, null=True)),
                ('expense_flag', models.BooleanField(blank=True, default=False, null=True)),
                ('income_flag', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('age', models.CharField(blank=True, max_length=400, null=True)),
                ('remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('place', models.CharField(blank=True, max_length=400, null=True)),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('other_contact', models.CharField(blank=True, max_length=400, null=True)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('submit_date', models.DateField(blank=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CounterValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docter_count', models.CharField(blank=True, max_length=400, null=True)),
                ('department_count', models.CharField(blank=True, max_length=400, null=True)),
                ('reserchlab_count', models.CharField(blank=True, max_length=400, null=True)),
                ('awards_count', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='doctors/')),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('email', models.EmailField(blank=True, max_length=400, null=True)),
                ('designation', models.CharField(blank=True, max_length=400, null=True)),
                ('snippets', models.CharField(blank=True, max_length=400, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=400, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=400, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=400, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='feedback/')),
                ('Role', models.CharField(blank=True, max_length=400, null=True)),
                ('snippets', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='GoogleMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('link', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('email', models.CharField(blank=True, max_length=400, null=True)),
                ('subject', models.CharField(blank=True, max_length=1000, null=True)),
                ('message', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(blank=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_body', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('age', models.CharField(blank=True, max_length=400, null=True)),
                ('place', models.CharField(blank=True, max_length=400, null=True)),
                ('username', models.CharField(blank=True, max_length=1000, null=True)),
                ('password', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(blank=True, max_length=400, null=True)),
                ('mobile1', models.CharField(blank=True, max_length=400, null=True)),
                ('remark', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(blank=True, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True)),
                ('is_nurse', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('age', models.CharField(blank=True, max_length=400, null=True)),
                ('remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('place', models.CharField(blank=True, max_length=400, null=True)),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('other_contact', models.CharField(blank=True, max_length=400, null=True)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('submit_date', models.DateField(blank=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuickAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('age', models.CharField(blank=True, max_length=400, null=True)),
                ('remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('place', models.CharField(blank=True, max_length=400, null=True)),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('other_contact', models.CharField(blank=True, max_length=400, null=True)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('submit_date', models.DateField(blank=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=400, null=True)),
                ('item_Image', models.ImageField(upload_to='shop/')),
                ('price', models.CharField(blank=True, max_length=400, null=True)),
                ('offer_price', models.CharField(blank=True, max_length=400, null=True)),
                ('category', models.CharField(blank=True, max_length=400, null=True)),
                ('discription', models.CharField(blank=True, max_length=1000, null=True)),
                ('rating', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('product_id', models.CharField(blank=True, max_length=400, null=True)),
                ('price', models.CharField(blank=True, max_length=400, null=True)),
                ('offer_price', models.CharField(blank=True, max_length=400, null=True)),
                ('shop_status', models.CharField(blank=True, max_length=400, null=True)),
                ('request_date', models.DateField(auto_now_add=True)),
                ('is_read', models.BooleanField(blank=True, default=False, null=True)),
                ('is_delivered', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.CharField(blank=True, max_length=400, null=True)),
                ('facebook', models.CharField(blank=True, max_length=400, null=True)),
                ('instagram', models.CharField(blank=True, max_length=400, null=True)),
                ('google_plus', models.CharField(blank=True, max_length=400, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(blank=True, max_length=400, null=True)),
                ('todo_dead_time', models.CharField(blank=True, max_length=400, null=True)),
                ('todo_subject', models.CharField(blank=True, max_length=400, null=True)),
                ('todo_body', models.CharField(blank=True, max_length=400, null=True)),
                ('todo_status', models.CharField(blank=True, max_length=400, null=True)),
                ('submit_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
