from django.urls import path
from django.shortcuts import render
from . import views
app_name = 'account'

urlpatterns = [
    # Registration
    path('register/', views.register_user, name='register'),
    path('email-verification-sent/',
         lambda request: request.render('account/registration/email-verification-sent.html'),
         name='email-verification-sent'
         ),
    # Login and logout
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Dashboard
    path('dasboard/', views.dashboard_user, name='dashboard'),
    path('profile-management/', views.profile_user, name='profile-management'),
    path('delete-user/', views.delete_user, name='delete-user'),

]
