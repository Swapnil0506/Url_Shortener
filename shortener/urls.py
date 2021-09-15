from django.urls import path
from . import views

urlpatterns = [
    path('', views.url, name='url'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]