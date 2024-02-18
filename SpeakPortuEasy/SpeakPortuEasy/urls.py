"""
URL configuration for SpeakPortuEasy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from main.views import index, register_student, register_class, register_schedule, register_classroom, register_enrollments, register_users, register_profiles, register_parents, register_zipcode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    path('register-student/', register_student),
    path('register-class/', register_class),
    path('register-schedule/', register_schedule),
    path('register-classroom/', register_classroom),
    path('register-enrollments/', register_enrollments),
    path('register-users/', register_users),
    path('register-profiles/', register_profiles),
    path('register-parents/', register_parents),
    path('register-zipcode/', register_zipcode),
    path('', index)
]
