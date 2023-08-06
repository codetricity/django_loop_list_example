from django.contrib import admin
from django.urls import path
from . import views

app_name='article'

urlpatterns = [
    path('<int:id>/', views.detail, name="detail")
]
