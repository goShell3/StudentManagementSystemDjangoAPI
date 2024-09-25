from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register_student, name='register_student'),
    path('success/', views.success_view, name='success'),
    # path('instructor_register/', views.register_instructor, name='register_instructor'),
    path('student_management/', views.student_management, name='student_management'),
    path('student_search/', views.student_search_byname, name='student_search_byname'),
]
