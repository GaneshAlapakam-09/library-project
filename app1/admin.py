from django.contrib import admin

from app1.models import Student,BookManagement
# Register your models here.
admin.site.register(Student)
admin.site.register(BookManagement)