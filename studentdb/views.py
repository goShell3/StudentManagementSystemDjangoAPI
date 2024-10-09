from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm, InstructorRegistrationForm
from .models import Student, Instructor


# sends a form data to the database  #add student 
@csrf_protect
def student_form_list(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        if student_form.is_valid():
            student_form_instance = student_form.save()
            data = {
                'student': {
                    'id': student_form_instance.id,
                    'first_name':student_form_instance.first_name,
                    'last_name':student_form_instance.last_name,
                    'email':student_form_instance.email,
                    'address':student_form_instance.address,
                    'city':student_form_instance.city,
                    'state':student_form_instance.state,
                    'date_of_birth':student_form_instance.data_of_birth,
                    'gender':student_form_instance.gender,
                    'student_department':student_form_instance.student_department
                },
                'status': 'success',
                'message': 'Forms saved successfully and protected with csrf'
            }
            return JsonResponse(data, status=200)
        # If forms are invalid, return the errors
        else:
            data = {
                'status': 'error',
                'student_errors': student_form.errors,
            }
            return JsonResponse(data, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
        
def StudentEditView(request, pk):
    if request.method == "PUT" or request.method == "POST":
        student = get_object_or_404(Student, pk=pk)
        data = request.POST.dict()

        form = StudentRegistrationForm(data, instance=student)

        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success', 
                'message': 'Student updated successfully'})
        else:
            return JsonResponse({
                'status': 'error', 
                'errors': form.errors}, 
                status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt     
def StudentDeleteView(request, pk):
    if request.method == "PUT":
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return JsonResponse({'status': 'success', 'message': 'Student deleted successfully'}, status=200)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



#List the list of student 
def listStudents(request):
    students = Student.objects.all().values('student_id', 'first_name', 'last_name', 'student_department')
    return JsonResponse(list(students), safe=False)


#form handler for instructor 
@csrf_protect
def instructor_form_list(request):
    if request.method == "POST":
        instructor_form = InstructorRegistrationForm(request.POST)
        if instructor_form.is_valid():
            instructor_form_instance = instructor_form.save()

            data = {
                'instractor': {
                    'id':instructor_form_instance.id,
                    'instructor_first_name':instructor_form_instance.instructor_form_instance,
                    'instructor_last_name':instructor_form_instance.instructor_last_name,
                    'instructor_email':instructor_form_instance.instructor_email,
                    'instructor_phone':instructor_form_instance.instructor_phone,
                    'instructor_department':instructor_form_instance.instructor_department
                },
                'status' :'success',
                'message': 'Form saved sucessfully'
            }

            return JsonResponse(data, status=200)
        
        else:
            data = {
                'status': 'error',
                'student_errors': instructor_form.errors,
            }
            return JsonResponse(data, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
        

def student_search_byname(request):
    if request.method == "GET":
        student_name = request.GET.get('name') 
        students = Student.objects.filter(name__icontains=student_name)  
        return render(request, 'StudentMS.html', {'students': students})
    return render(request, 'studentMS.html')

def department_instructor(request):
    if request.method == "GET":
        department_name = request.GET.get('department')  # Get the department from the query
        students = Student.objects.filter(department_name__icontains=department_name)  # Filter students by department
        
        instructors = Instructor.objects.filter(department_name__icontains=department_name).prefetch_related('students')  # Join instructors with their students
        
        return render(request, 'student_search.html', {'students': students, 'instructors': instructors})  # Render both students and instructors


# views 