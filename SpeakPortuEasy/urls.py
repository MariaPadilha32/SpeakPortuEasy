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
from accounts import views as v_accounts
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', vw.index, name="home"),
    path('register-student/', vw.register_student, name="register-student"),
    path('register-class/', vw.register_class, name="register-class"),
    path('register-classroom/',
         vw.register_classroom,
         name="register-classroom"
         ),
    path('register-enrollments/',
         vw.register_enrollments,
         name="register-enrollments"
         ),
    path('register-parents/', vw.register_parents, name="register-parents"),
    path('query-class/', vw.query_class, name="query-class"),
    path('query-classroom/', vw.query_classroom, name="query-classroom"),
    path('query-enrollments/', vw.query_enrollments, name="query-enrollments"),
    path('query-parents/', vw.query_parents, name="query-parents"),
    path('query-student/', vw.query_student, name="query-student"),
    path('query-users/', vw.query_users, name="query-users"),
    path('delete-student/<int:id>', vw.delete_student, name="delete-student"),
    path('delete-class/<int:id>', vw.delete_class, name="delete-class"),
    path('delete-classroom/<int:id>',
         vw.delete_classroom,
         name="delete-classroom"
         ),
    path('delete-enrollments/<int:id>',
         vw.delete_enrollments,
         name="delete-enrollments"
         ),
    path('delete-users/<int:id>', vw.delete_users, name="delete-users"),
    path('delete-parents/<int:id>', vw.delete_parents, name="delete-parents"),
    path('edit-student/<int:id>', vw.edit_student, name="edit-student"),
    path('edit-class/<int:id>', vw.edit_class, name="edit-class"),
    path('edit-classroom/<int:id>', vw.edit_classroom, name="edit-classroom"),
    path('edit-enrollments/<int:id>/',
         vw.edit_enrollments,
         name="edit-enrollments"
         ),
    path('edit-users/<int:id>', vw.edit_users, name="edit-users"),
    path('edit-parents/<int:id>', vw.edit_parents, name="edit-parents"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', v_accounts.register, name='register'),
    path('recover-password/', vw.recover_password, name="recover-password"),
    path('register-teacher/', vw.register_teacher, name="register-teacher"),
    path('query-teacher/', vw.query_teacher, name="query-teacher"),
    path('edit-teacher/<int:id>', vw.edit_teacher, name="edit-teacher"),
    path('delete-teacher/<int:id>', vw.delete_teacher, name="delete-teacher"),
    path('search-classroom/', vw.search_classroom, name='search-classroom'),
    path('search-class/', vw.search_class, name='search-class'),
    path('search-student/', vw.search_student, name='search-student'),
    path('search-enrollments/',
         vw.search_enrollments,
         name='search-enrollments'
         ),
    path('search-parents/', vw.search_parents, name='search-parents'),
    path('search-teacher/', vw.search_teacher, name='search-teacher'),
    path('', vw.index, name="")
]


handler404 = vw.v_404
handler500 = vw.v_500
# vw.v_404 = 'error404.html'
