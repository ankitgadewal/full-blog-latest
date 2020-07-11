"""practice3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('topsecretoftheweb/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html', success_url='/password_change_done'), name='change_password'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='change_password_done'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('premium_info', user_views.premium_info, name='premium_info'),
    path('premium/', user_views.premium, name='premium'),
    path('premium/handle_request/', user_views.handle_request, name='handle_request'),
    path('fb-login/', include('social_django.urls', namespace='fb-login')),
    path('contactme', user_views.ContactMe.as_view(), name='contact-me'),
    path('', include('app1.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
