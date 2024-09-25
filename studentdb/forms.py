from django import forms
from .models import Student, Instructor

#views for student registration
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'date_of_birth', 'gender']
        labels = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Email address',
            'phone': 'Enter your phone number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender'
        }
        error_messages = {
            'first_name': {
                'required': 'First name is required.',
            },
            'last_name': {
                'required': 'Last name is required.',
            },
            'email': {
                'required': 'Email address is required.',
                'invalid': 'Please enter a valid email address.'
            },
            'phone': {
                'required': 'Phone number is required.',
            },
            'address': {
                'required': 'Address is required.'
            },
            'city': {
                'required': 'City is required.',
            },
            'state': {
                'required': 'State is required.',
            },
            'date_of_birth': {
                'required': 'Date of birth is required.',
                'invalid': 'Please enter a valid date.'
            },
            'gender': {
                'required': 'Gender is required.',
            }
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("A student with this email already exists.")
        return email

class InstructorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Instructor 
        fields = {'instructor_first_name', 'instructor_last_name', 'instructor_email', 'instructor_phone', 'instructor_department'}
        labels = {
            'instructor_first_name': 'Enter your name',
            'instructor_last_name' : 'Enter your last name',
            'instructor_email' : 'Enter your email',
            'instructor_phone' : 'Enter your phone number',
            'instructor_department' : 'Enter your department'
        }
