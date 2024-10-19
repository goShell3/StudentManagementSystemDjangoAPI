from django.db import models

class Department(models.Model):
    DEPARTMENT_TYPES = [
        ('COMP', 'Computer Science'),
        ('IOS', 'Information Science'),
        ('BNS', 'College of Business'),
        ('SWR', 'Software Science'),
        ('ENG', 'Engineering'),
    ]
    
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=200, choices=DEPARTMENT_TYPES)
    department_description = models.CharField(max_length=200)

    def __str__(self):
        return self.get_department_name_display()


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    student_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    date_of_birth = models.DateField( )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    instructor_first_name = models.CharField(max_length=200)
    instructor_last_name = models.CharField(max_length=200)
    instructor_email = models.EmailField(max_length=200, unique=True)
    instructor_phone = models.CharField(max_length=200)
    instructor_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='instructors')

    def __str__(self):
        return f'{self.instructor_first_name} {self.instructor_last_name} '


class Course(models.Model):

    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_description = models.CharField(max_length=500)
    course_credit = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='courses')
    instructors = models.ManyToManyField(Instructor, related_name='courses')

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):

    enrollment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f'{self.student.first_name} enrolled in {self.course.course_name}'

