from django.contrib import admin
from django.urls import path
from . import views

app_name='article'

urlpatterns = [
    path('<slug:post>/', views.detail, name="detail")
]
