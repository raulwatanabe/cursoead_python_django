from django.urls import path

from . import views

urlpatterns = [
        path('contato/', views.contact, name='contact'),
        path('', views.home, name='home'),
]

