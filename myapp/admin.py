from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['pic','name','age','birth','language','address','email','phone','added']
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','groupscount']
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','teacher','education','start','added']