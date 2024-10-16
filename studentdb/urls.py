from django.urls import path
from . import views

urlpatterns = [
    path('student_form_handler/', views.student_form_list, name='student_form_handler'),
    path('student_lists/', views.listStudents, name="student_list_handler"),
    path('students/<int:pk>/edit/', views.StudentEditView, name='student_edit'),
    path('students/<int:student_id>/remove_student', views.StudentDeleteView, name='student_delete'),
    path('instructor_course_list/<int:pk>/', views.InstructorCourseList, name= "instructor-course_list"),
    path('instructor_form_hanlder/', views.instructor_form_list, name='instructor_form_handler'),
    path('department_list/<int:pk>/', views.ListDepartment, name="list_departments_pk")
]