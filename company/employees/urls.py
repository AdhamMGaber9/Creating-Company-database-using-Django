from django.urls import path
# from company.employees.views import employees_list, delete_employees, show_employee
from employees.views import employees_list, employee_delete ,employee_show,create_employee,edit_employee
from django.urls import path

urlpatterns = [
    path('index',employees_list, name='employees.index'),
    path('index/<int:id>/delete',employee_delete, name='employees.delete'),
    path('index/<int:id>/show',employee_show, name='employees.show'),
    # path('index', emoloyees_index, name='employees.index'),
    path('create',create_employee,name='employees.create'),
    path('index/<int:id>/edit',edit_employee, name='employees.edit'),
]