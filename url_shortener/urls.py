from django.contrib import admin
from django.urls import path
from app.views import shorten_url, redirect_to_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/', redirect_to_url, name='redirect_to_url'),
]
