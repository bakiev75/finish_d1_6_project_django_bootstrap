"""finish_d1_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Для итогового задания добавляю три странички.
    path('page_1/', include('django.contrib.flatpages.urls')), # Будет установлен доступ по паролю администратора
    path('page_2/', include('django.contrib.flatpages.urls')), # Будут изменены шрифты и размер текста
    path('page_3/', include('django.contrib.flatpages.urls')), # контент дублируется без изменения content
    path('page_home/', include('django.contrib.flatpages.urls'))
]
