from django.urls import path
from cse import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/admin',views.adminlogin,name="adminlogin")
]