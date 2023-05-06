from departments.views import departments_index , show_dept, delete_dept, edit_dept, create_dept

from django.urls import path

urlpatterns = [
    path('index',departments_index, name='department.index'),
    path('index/<int:id>/delete',delete_dept, name='department.delete'),
    path('index/<int:id>/show',show_dept, name='department.show'),
    path('index/<int:id>/edit',edit_dept, name='department.edit'),
    path('create',create_dept,name='department.create'),
]