from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome_partial, name='load-welcome'),
]
