from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users.forms import UserLoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),    
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=UserLoginForm),name='login'),
]
