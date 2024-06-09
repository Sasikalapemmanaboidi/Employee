from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Employee, Address, WorkExperience, Qualification, Project
from django.db import transaction, IntegrityError


def employee_createlabel(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Get the user data
                username = request.POST['username']
                email = request.POST['email']
                age = request.POST['age']
                gender = request.POST['gender']
                phoneNo = request.POST['phoneNo']
                photo = request.FILES.get('photo')

                # Get the address data
                hno = request.POST['hno']
                street = request.POST['street']
                city = request.POST['city']
                state = request.POST['state']

                # Get the work experience data
                companyName = request.POST['companyName']
                fromDate = request.POST['fromDate']
                toDate = request.POST['toDate']
                job_location = request.POST['job_location']

                # Get the qualification data
                qualificationName = request.POST['qualificationName']
                percentage = request.POST['percentage']

                # Get the project data
                title = request.POST['title']
                description = request.POST['description']

                # Create Address instance
                address = Address(hno=hno, street=street, city=city, state=state)
                address.save()

                # Create WorkExperience instance
                work_experience = WorkExperience(companyName=companyName, fromDate=fromDate, toDate=toDate, job_location=job_location)
                work_experience.save()

                # Create Qualification instance
                qualification = Qualification(qualificationName=qualificationName, percentage=percentage)
                qualification.save()

                # Create Project instance
                project = Project(title=title, description=description)
                project.save()

                # Create User instance
                user = User.objects.create_user(username=username, email=email)
                user.save()

                # Create Employee instance
                employee = Employee(user=user, username=username, email=email, age=age, gender=gender, phoneNo=phoneNo,
                                    address=address, workExperience=work_experience, qualifications=qualification,
                                    projects=project, photo=photo)
                employee.save()

                messages.success(request, 'Employee added successfully!')
                return redirect('employee:employee_createlabel')

        except IntegrityError as e:
            messages.error(request, f'Error adding employee: {e}')
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {e}')
            
    return render(request, 'employee_createlabel.html')


def employee_editlabel(request, username):
    
    employee = get_object_or_404(Employee, username=username)
    if request.method == 'POST':
        try:
          employee.username = request.POST.get('username')
          employee.email = request.POST.get('email')
          employee.age = request.POST.get('age')
          employee.gender = request.POST.get('gender')
          employee.phoneNo = request.POST.get('phoneNo')
          
          try:
                if request.FILES.get('photo'):
                    employee.photo = request.FILES('photo')
                else:
                    value = Employee.get('photo', 'null')
                    employee.photo = value 
          except:
                pass
            
          
          # Update address
          employee.address.hno = request.POST.get('hno')
          employee.address.street = request.POST.get('street')
          employee.address.state = request.POST.get('state')
          employee.address.city = request.POST.get('city')
          
          # Update work experience
          employee.workExperience.companyName = request.POST.get('companyName')
          try:
              if request.POST['fromDate'] == "":
                  value = WorkExperience.get('fromDate', None)
                  employee.workExperience.fromDate = value 
              else:
                  employee.workExperience.fromDate =  request.POST['fromDate']
          except:
              pass
          try:
              if request.POST['toDate'] == "":
                  value = WorkExperience.get('toDate', None)
                  employee.workExperience.toDate = value 
              else:
                  employee.workExperience.toDate =  request.POST['toDate']
          except:
              pass
          employee.workExperience.job_location = request.POST.get('job_location')
          
          # Update qualifications
          employee.qualifications.qualificationName = request.POST.get('qualificationName')
          employee.qualifications.percentage = request.POST.get('percentage')
          
          # Update projects
          employee.projects.title = request.POST.get('title')
          employee.projects.description = request.POST.get('description')
          
          # Save all changes
          employee.save()
          employee.address.save()
          employee.workExperience.save()
          employee.qualifications.save()
          employee.projects.save()
        
          # Save changes to the employee
          employee.save()
          return JsonResponse({'message': 'Employee details updated successfully!'})
        except Exception as e:
            # Return error message if there's an issue with updating
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'employee_editlabel.html', {'employee': employee})



def employee_content(request):
    employees = Employee.objects.select_related('address', 'workExperience', 'qualifications', 'projects').all()
    context = {
      'employee_content': employees,
    }
    return render(request, 'employee_content.html', context)

def employee_delete(request, username):
    # Find the employee by username or return 404 if not found
    employee = get_object_or_404(Employee, username=username)

    # Delete the employee
    user = employee.user

    # Delete the user, which will also delete the employee due to on_delete=models.CASCADE
    user.delete()
    employee.delete()
    employee.address.delete()
    employee.workExperience.delete()
    employee.qualifications.delete()
    employee.projects.delete()
    
    # Return a simple HttpResponse with a success message
    return HttpResponse("Employee deleted successfully.")