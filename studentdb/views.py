from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .forms import StudentRegistrationForm, InstructorRegistrationForm
from .models import Student, Instructor, Department
# from django.views.generic import DetailView


# sends a form data to the database  #add student 
@csrf_protect
def student_form_list(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        if student_form.is_valid():
            student_form_instance = student_form.save()
            data = {
                'student': {
                    'id': student_form_instance.student_id,
                    'first_name': student_form_instance.first_name,
                    'last_name': student_form_instance.last_name,
                    'email': student_form_instance.email,
                    'phone': student_form_instance.phone,
                    'address': student_form_instance.address,
                    'city': student_form_instance.city,
                    'state': student_form_instance.state,
                    'date_of_birth': student_form_instance.date_of_birth,
                    'gender': student_form_instance.gender,
                    'student_department': student_form_instance.student_department.department_name,
                },
                'status': 'success',
                'message': 'Form saved successfully and protected with CSRF'
            }
            return JsonResponse(data, status=200)
        else:
            data = {
                'status': 'error',
                'student_errors': student_form.errors,
            }
            return JsonResponse(data, status=400)

    elif request.method == 'GET':
        form_fields = {
            'first_name': 'string',
            'last_name': 'string',
            'email': 'string',
            'phone': 'string',
            'address': 'string',
            'city': 'string',
            'state': 'string',
            'date_of_birth': 'date (YYYY-MM-DD)',
            'gender': ['M', 'F'],  # Assuming these are the choices
            'student_department': [dept.department_name for dept in Department.objects.all()]  # List of department choices
        }
        data = {
            'status': 'success',
            'message': 'Form fields available for POST request',
            'fields': form_fields
        }
        return JsonResponse(data, status=200)

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
    if request.method == "DELETE":
        student = get_object_or_404(Student, student_id=pk)
        student.delete()
        return JsonResponse({'status': 'success', 'message': 'Student deleted successfully'}, status=200)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

#List the list of student 
def listStudents(request):
    if request.method == "GET":
        students = Student.objects.all().values('student_id', 'first_name', 'last_name', 'student_department')
        return JsonResponse(list(students), safe=False)

#List all Instructor 
def ListInstructor(request):
    if request.method == "GET":
        instructor = Instructor.objects.all().value('instructor_id', 'instructor_first_name', 'instructor_last_name', 'instructor_email', 'instructor_phone', 'instructor_department')
        return JsonResponse(list(instructor), safe=False)  

#GET instructors list based on cousses
def InstructorCourseList(request, pk):
    if request.method == "GET":
        instructor_instance = Instructor.objects.filter(instructor_department_id=pk).values("instructor_first_name", "instructor_last_name", "instructor_department")
        return JsonResponse(list(instructor_instance), safe=False)        

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
         
# GET all the list of department by primary key
def ListDepartment(request, pk):
    if request.method == "GET":
        department = Department.objects.filter(department_id=pk).value("departement_id", "department_name", "department_description" )
        return JsonResponse(list(department), safe=False)
    else:
        return JsonResponse({'status':'error', 'message':'Invalid request method'}, status=405)
