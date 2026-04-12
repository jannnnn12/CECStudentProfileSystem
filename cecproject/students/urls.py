from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/',  views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Student Registration (Public)
    path('register/',           views.student_register,       name='student_register'),
    path('register/success/<int:pk>/', views.student_register_success, name='student_register_success'),

    # Students (Admin/Dashboard)
    path('',                      views.student_list,   name='student_list'),
    path('student/<int:pk>/',     views.student_detail, name='student_detail'),
    path('student/add/',          views.student_add,    name='student_add'),
    path('student/<int:pk>/edit/',   views.student_edit,   name='student_edit'),
    path('student/<int:pk>/inactive/', views.student_set_inactive, name='student_set_inactive'),
    path('student/<int:pk>/active/',   views.student_set_active,   name='student_set_active'),
]
