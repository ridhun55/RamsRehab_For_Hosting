from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeApp.urls')),
    path('administration/', include('AdministrationApp.urls')),
    path('blog/', include('TheBlog.urls')),

    path('login/', include('django.contrib.auth.urls')),
    path('login/', include('LoginApp.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)