from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from .views import CategoryListView



urlpatterns = [
    path('category/',CategoryListView.as_view(), name='category_api'),
]
