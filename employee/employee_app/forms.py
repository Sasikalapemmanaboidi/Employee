from django import forms
from django.contrib.auth.models import User
from .models import Address, WorkExperience, Qualification, Project, Employee

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['age', 'gender', 'phoneNo', 'photo']

class CompositeEmployeeForm(forms.Form):
    user = UserForm()
    address = AddressForm()
    work_experience = WorkExperienceForm()
    qualification = QualificationForm()
    project = ProjectForm()
    employee = EmployeeForm()

    def save(self, commit=True):
        user = self.cleaned_data['user']
        address = self.cleaned_data['address']
        work_experience = self.cleaned_data['work_experience']
        qualification = self.cleaned_data['qualification']
        project = self.cleaned_data['project']
        employee = self.cleaned_data['employee']

        if commit:
            user.save()
            address.save()
            work_experience.save()
            qualification.save()
            project.save()
            employee.user = user
            employee.address = address
            employee.workExperience = work_experience
            employee.qualifications = qualification
            employee.projects = project
            employee.save()

        return employee
