from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.html import format_html
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 150,null=True,blank=True)
    age = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='student-images',blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    type = (
        ('uzbek','Uzbek'),
        ('rus','Rus')
    )
    language = models.CharField(max_length=10,choices=type,default='uzbek')
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20,null=True,blank=True,verbose_name="Phone number",help_text="Ënter student number")
    added = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    @property
    def pic(self):
        if self.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
        else:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format('https://img.freepik.com/premium-photo/graduation-student-standing-with-diploma_255667-15599.jpg'))
    @property
    def groupscount(self):
        return len(self.groups.all())
    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    @property
    def groupscount(self):
        return len(self.groups.all())
class Group(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    student = models.ManyToManyField(Student,related_name='groups')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='groups', blank=True, null=True)
    class Type(models.TextChoices):
        offline = 'offline','Offline'
        online = 'online','Online'
    
    my_choice = (
        ('dushanba','Dushanba'),
        ('seshanba','Seshanba'),
        ('chorshanba','Chorshanba'),
        ('payshanba','Payshanba'),
        ('juma','Juma'),
        ('shanba','Shanba'),
        ('yakshanba','Yakshanba'),
    )
    start = models.DateField()
    day = MultiSelectField(choices=my_choice,max_length=100)
    teacher = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=10,choices=Type.choices,default='offline')
    added = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    @property
    def studentscount(self):
        return len(self.student.all())
    def __str__(self):
        return self.name