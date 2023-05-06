from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from departments.models import Department
from departments.forms import DepartmentForm

def alldepartments(request):
    departments=Department.get_all_departments()
    return HttpResponse(departments)
def departments_index(request):
    departments =Department.get_all_departments()
    return render(request, 'departments.html',context={"alldepartments":departments})



def show_dept(request, id):
    department = Department.get_department(id)
    return render(request, 'department_info.html',context={"department": department})


def delete_dept(request, id):
    department = Department.get_department(id)
    department.delete()
    redirect_url = reverse('department.index')
    return redirect(redirect_url)

def create_dept(request):
    form = DepartmentForm()
    print("hi")
    if request.method =='GET':
        print("get")
        return render(request, 'create_employee.html', context={"form":form})
    else:
        print(request.POST)

        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        redirect_url = reverse('department.index')
        return redirect(redirect_url)
def edit_dept(request, id ):
    department = Department.get_department(id)
    if request.method =='GET':
        form = DepartmentForm(instance=department)
        return render(request, 'edit_department.html', context={"form":form})
    else:
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
        redirect_url = reverse('department.show',args=[department.id])
        return redirect(redirect_url)