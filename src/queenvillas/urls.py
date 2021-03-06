"""queenvillas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import home_page,handle_signup,handle_login,handle_logout,contact_page
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name="home"),
    path('residential/', include(("residential.urls", "residential"), namespace='residentials')),
    path('signup', handle_signup, name="signup"),
    path('login', handle_login, name="login"),
    path('logout', handle_logout, name="logout"),
    path('search/', include(("search.urls","search"),namespace="search")),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='pwd_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='pwd_reset_view.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='pwd_reset_done.html'),name='password_reset_complete'),
    path('contact',contact_page,name="contact")
]

if settings.DEBUG:
    urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)