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
from django.urls import path, include
from django.contrib.auth import views
import main.views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', vw.index, name="home"),
    path('register-student/', vw.register_student, name="register-student"),
    path('register-class/', vw.register_class, name="register-class"),
    path('register-schedule/', vw.register_schedule, name="register-schedule"),
    path('register-classroom/', vw.register_classroom, name="register-classroom"),
    path('register-enrollments/', vw.register_enrollments, name="register-enrollments"),
    path('register-users/',vw.register_users, name="register-users"),
    path('register-profiles/', vw.register_profiles, name="register-profiles"),
    path('register-parents/', vw.register_parents, name="register-parents"),
    path('register-zipcode/', vw.register_zipcode, name="register-zipcode"),
    path('query-class/', vw.query_class, name="query-class"),
    path('query-classroom/', vw.query_classroom, name="query-classroom"),
    path('query-enrollments/', vw.query_enrollments, name="query-enrollments"),
    path('query-parents/', vw.query_parents, name="query-parents"),
    path('query-profiles/', vw.query_profiles, name="query-profiles"),
    path('query-schedule/', vw.query_schedule, name="query-schedule"),
    path('query-student/', vw.query_student, name="query-student"),
    path('query-users/', vw.query_users, name="query-users"),
    path('query-zipcode/', vw.query_zipcode, name="query-zipcode"),
    path('delete-student/<int:id>', vw.delete_student, name="delete-student"),
    path('delete-class/<int:id>', vw.delete_class, name="delete-class"),
    path('delete-schedule/<int:id>', vw.delete_schedule, name="delete-schedule"),
    path('delete-classroom/<int:id>', vw.delete_classroom, name="delete-classroom"),
    path('delete-enrollments/<int:id>', vw.delete_enrollments, name="delete-enrollments"),
    path('delete-users/<int:id>', vw.delete_users, name="delete-users"),
    path('delete-profiles/<int:id>', vw.delete_profiles, name="delete-profiles"),
    path('delete-parents/<int:id>', vw.delete_parents, name="delete-parents"),
    path('delete-zipcode/<int:id>', vw.delete_zipcode, name="delete-zipcode"),
    path('edit-student/<int:id>', vw.edit_student, name="edit-student"),
    path('edit-class/<int:id>', vw.edit_class, name="edit-class"),
    path('edit-schedule/<int:id>', vw.edit_schedule, name="edit-schedule"),
    path('edit-classroom/<int:id>', vw.edit_classroom, name="edit-classroom"),
    path('edit-enrollments<int:id>/', vw.edit_enrollments, name="edit-enrollments"),
    path('edit-users/<int:id>', vw.edit_users, name="edit-users"),
    path('edit-profiles/<int:id>', vw.edit_profiles, name="edit-profiles"),
    path('edit-parents/<int:id>', vw.edit_parents, name="edit-parents"),
    path('edit-zipcode/', vw.edit_zipcode, name="edit-zipcode"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('recover-password/', vw.recover_password, name="recover-password"),
    path('', vw.index, name="")
]
