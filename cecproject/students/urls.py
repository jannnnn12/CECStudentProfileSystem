from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/',  views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Students
    path('',                      views.student_list,   name='student_list'),
    path('student/<int:pk>/',     views.student_detail, name='student_detail'),
    path('student/add/',          views.student_add,    name='student_add'),
    path('student/<int:pk>/edit/',   views.student_edit,   name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
