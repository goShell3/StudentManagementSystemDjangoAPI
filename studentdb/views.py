from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm, InstructorRegistrationForm
from .models import Student, Instructor


def student_management(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        instructor_form = InstructorRegistrationForm(request.POST)
        if student_form.is_valid() and instructor_form.is_valid():
            student_form.save()
            instructor_form.save()
            return redirect('success')  # Replace with your success URL
    else:
        student_form = StudentRegistrationForm()
        instructor_form = InstructorRegistrationForm()

    context = {
        'student_form': student_form,
        'instructor_form': instructor_form,
    }
    return render(request, 'StudentMS.html', context)

def success_view(request):
    return HttpResponse("Student registered successfully!")

def student_search_byname(request):
    if request.method == "GET":
        student_name = request.GET.get('name') 
        students = Student.objects.filter(name__icontains=student_name)  
        return render(request, 'StudentMS.html', {'students': students})
    return render(request, 'student_search.html')

def department_instructor(request):
    if request.method == "GET":
        department_name = request.GET.get('department')  # Get the department from the query
        students = Student.objects.filter(department_name__icontains=department_name)  # Filter students by department
        
        # Assuming you have an Instructor model related to Student
        instructors = Instructor.objects.filter(department_name__icontains=department_name).prefetch_related('students')  # Join instructors with their students
        
        return render(request, 'student_search.html', {'students': students, 'instructors': instructors})  # Render both students and instructors

