from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    
    path('', views.job_list),
    path('<int:id>',views.job_details),
]
