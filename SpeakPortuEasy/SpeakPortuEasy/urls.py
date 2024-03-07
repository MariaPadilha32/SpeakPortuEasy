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
from main.views import index, register_student, register_class, register_schedule, register_classroom, register_enrollments, register_users, register_profiles, register_parents, register_zipcode, query_class, query_classroom, query_enrollments, query_parents, query_profiles, query_schedule, query_student, query_users, query_zipcode, delete_class, delete_classroom, delete_enrollments, delete_parents, delete_profiles, delete_schedule, delete_student, delete_users, delete_zipcode, edit_class, edit_classroom, edit_enrollments, edit_parents, edit_profiles, edit_schedule, edit_student, edit_users, edit_zipcode
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index, name="home"),
    path('register-student/', register_student, name="register-student"),
    path('register-class/', register_class, name="register-class"),
    path('register-schedule/', register_schedule, name="register-schedule"),
    path('register-classroom/', register_classroom, name="register-classroom"),
    path('register-enrollments/', register_enrollments, name="register-enrollments"),
    path('register-users/', register_users, name="register-users"),
    path('register-profiles/', register_profiles, name="register-profiles"),
    path('register-parents/', register_parents, name="register-parents"),
    path('register-zipcode/', register_zipcode, name="register-zipcode"),
    path('query-class/', query_class, name="query-class"),
    path('query-classroom/', query_classroom, name="query-classroom"),
    path('query-enrollments/', query_enrollments, name="query-enrollments"),
    path('query-parents/', query_parents, name="query-parents"),
    path('query-profiles/', query_profiles, name="query-profiles"),
    path('query-schedule/', query_schedule, name="query-schedule"),
    path('query-student/', query_student, name="query-student"),
    path('query-users/', query_users, name="query-users"),
    path('query-zipcode/', query_zipcode, name="query-zipcode"),
    path('delete-student/', delete_student, name="delete-student"),
    path('delete-class/', delete_class, name="delete-class"),
    path('delete-schedule/', delete_schedule, name="delete-schedule"),
    path('delete-classroom/', delete_classroom, name="delete-classroom"),
    path('delete-enrollments/', delete_enrollments, name="delete-enrollments"),
    path('delete-users/', delete_users, name="delete-users"),
    path('delete-profiles/', delete_profiles, name="delete-profiles"),
    path('delete-parents/', delete_parents, name="delete-parents"),
    path('delete-zipcode/', delete_zipcode, name="delete-zipcode"),
    path('edit-student/', edit_student, name="edit-student"),
    path('edit-class/', edit_class, name="edit-class"),
    path('edit-schedule/', edit_schedule, name="edit-schedule"),
    path('edit-classroom/', edit_classroom, name="edit-classroom"),
    path('edit-enrollments/', edit_enrollments, name="edit-enrollments"),
    path('edit-users/', edit_users, name="edit-users"),
    path('edit-profiles/', edit_profiles, name="edit-profiles"),
    path('edit-parents/', edit_parents, name="edit-parents"),
    path('edit-zipcode/', edit_zipcode, name="edit-zipcode"),
    path('', index, name="")
]
