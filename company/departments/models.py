from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_departments(cls):
        return cls.objects.all()

    @classmethod
    def get_department(cls, id):
        return cls.objects.get(id=id)

    def get_delete_url(self):
        delete_url = reverse('department.delete', args=[self.id])
        return delete_url

    def get_show_url(self):
        show_url = reverse('department.show', args=[self.id])
        return show_url

    def get_edit_url(self):
        edit_url = reverse('department.edit', args=[self.id])
        return edit_url