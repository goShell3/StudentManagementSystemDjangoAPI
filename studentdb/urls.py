from django.urls import path
from . import views

urlpatterns = [
    path('student_form_handler/', views.student_form_list, name='form_handler'),
    # path('students/add/', views.StudentAddView, name='student_add'),
    path('students/<int:pk>/edit/', views.StudentEditView, name='student_edit'),
    # path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    # path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('instructor_form_hanlder/', views.instructor_form_list, name='form_handler')
]