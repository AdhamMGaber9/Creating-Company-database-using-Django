from django.shortcuts import render, redirect , reverse
from  django.http import HttpResponse
# Create your views here.
from  employees.models import Employee


# employees=  ['Ahmed', 'Mohamed', 'Gehad']
def allemployees(request):
    employees = Employee.get_all_employees()
    return HttpResponse(employees)


def getemployee(request, id):
    employees = Employee.get_all_employees()
    if id in range(len(employees)):
        return HttpResponse(employees[id])
    else:
        return HttpResponse("<h1> Student not found </h1>")

#

def employees_list(request):
    employees = Employee.get_all_employees()
    return render(request,'employees.html',context={"allemployees": employees})


def employee_delete(request, id):
    student = Employee.get_employee(id)
    student.delete()
    redirect_url = reverse('employees.index')
    return redirect(redirect_url)


def employee_show(request, id):
    employee = Employee.get_employee(id)
    return render(request, 'employee_info.html', context={"employee":employee})

#
from employees.forms import  EmployeeForm
def create_employee(request):
    form = EmployeeForm()
    print("hi")
    if request.method =='GET':
        print("get")
        return render(request, 'create_employee.html', context={"form":form})
    else:
        print(request.POST)
        ## upload image 000> request.FILES
        # print(request.FILES)
        ## use form object to save data
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # return HttpResponse("POST request received")
        redirect_url = reverse('employees.index')
        return redirect(redirect_url)

def edit_employee(request, id ):
    employee = Employee.get_employee(id)
    if request.method =='GET':
        form = EmployeeForm(instance=employee)
        return render(request, 'edit_employee.html', context={"form":form})
    else:
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
        redirect_url = reverse('employees.show',args=[employee.id])
        return redirect(redirect_url)