from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loginFun,name='login'),
    path('logout/',views.logoutFun,name='logout'),
]
