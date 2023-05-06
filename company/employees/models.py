from django.db import models
from django.urls import reverse
from departments.models import Department

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    dept = models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE,related_name='dept_emp')
    def __str__(self):
        return self.name

    @classmethod
    def get_all_employees(cls):
        return cls.objects.all()

    @classmethod
    def get_employee(cls, id):
        return cls.objects.get(id=id)

    def get_delete_url(self):
        delete_url = reverse('employees.delete', args=[self.id])
        return delete_url

    def get_show_url(self):
        show_url = reverse('employees.show', args=[self.id])
        return show_url

    def get_edit_url(self):
        edit_url = reverse('employees.edit', args=[self.id])
        return edit_url