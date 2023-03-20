from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['pic','name','age','birth','language','address','email','phone','groupscount','added']
    def has_change_permission(self,request,obj=None):
     if obj is not None and obj.user != request.user:
         return False
     return True
    def has_delete_permission(self,request,obj=None):
     if obj is not None and obj.user != request.user:
         return False
     return True
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','groupscount']
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','teacher','education','start','studentscount','added']
    def has_change_permission(self,request,obj=None):
     if obj is not None and obj.user != request.user:
         return False
     return True
    def has_delete_permission(self,request,obj=None):
     if obj is not None and obj.user != request.user:
         return False
     return True
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)