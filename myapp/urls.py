from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [

   
    path('hello/',views.hello,name='hello'),
    path('contact/',views.contact,name='contact'),
    path('newmember/',views.newmember,name='newmember'),
    path('hello/detail/<int:id>',views.detail,name='detail'),
    path('hello/detail/update/<int:id>',views.update,name="update"),
    path('hello/detail/delete/<int:id>',views.delete,name="delete"),
]