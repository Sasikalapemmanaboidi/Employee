from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Address(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    hno = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        db_table = 'address'

class WorkExperience(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    companyName = models.CharField(max_length=255)
    fromDate = models.DateField(null=True, blank=True)
    toDate = models.DateField(null=True, blank=True)
    job_location = models.CharField(max_length=255)

    class Meta:
        db_table = 'work_experience'

class Qualification(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    qualificationName = models.CharField(max_length=255)
    percentage = models.FloatField(null=True)

    class Meta:
        db_table = 'qualification'

class Project(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)

    class Meta:
        db_table = 'project'


# Employee model
def rename(instance, filename):
    return f'Users/{instance.user.username}/{filename}'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = PhoneNumberField(default=None)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    workExperience = models.OneToOneField(WorkExperience, on_delete=models.CASCADE)
    qualifications = models.OneToOneField(Qualification, on_delete=models.CASCADE)
    projects = models.ForeignKey('Project', on_delete=models.CASCADE,  default=1, verbose_name="project",  db_column='id')
    photo = models.ImageField(upload_to=rename, default='Users/blank_profile.webp', null=True)

    class Meta:
        db_table = 'employee'
