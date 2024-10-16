# Generated by Django 5.1.1 on 2024-10-12 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(choices=[('COMP', 'Computer Science'), ('IOS', 'Information Science'), ('BNS', 'College of Business'), ('SWR', 'Software Science'), ('ENG', 'Engineering')], max_length=200)),
                ('department_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.AutoField(primary_key=True, serialize=False)),
                ('instructor_first_name', models.CharField(max_length=200)),
                ('instructor_last_name', models.CharField(max_length=200)),
                ('instructor_email', models.EmailField(max_length=200, unique=True)),
                ('instructor_phone', models.CharField(max_length=200)),
                ('instructor_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructors', to='studentdb.department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200)),
                ('course_description', models.CharField(max_length=500)),
                ('course_credit', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='studentdb.department')),
                ('instructors', models.ManyToManyField(related_name='courses', to='studentdb.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('student_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='studentdb.department')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('enrollment_date', models.DateField()),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='studentdb.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='studentdb.student')),
            ],
        ),
    ]
