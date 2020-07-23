from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="Indexpage"),
    path('login', views.LoginUser, name="LoginPage"),
    path('logout', views.LogoutUser, name="LogoutPage"),
    path('signup', views.SignupUser, name="SignupPage"),
    path('change-password', views.ChangePassword, name="UsernameCheck"),
]