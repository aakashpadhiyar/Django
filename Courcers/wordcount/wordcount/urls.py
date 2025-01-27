from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count'),
    path('admin/', admin.site.urls),
]
