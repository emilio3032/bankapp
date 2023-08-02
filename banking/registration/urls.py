from . import views
from django.urls import path
app_name='registration'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form/',views.form,name='form'),
    path('forms/',views.forms,name='forms')
]