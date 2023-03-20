from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from .pagination import *
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    pagination_class = CustomPagination
class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        group  = Group.objects.get(id = data['name'])
       
        if 'subject' in data:
            try:
                subject = Subject.objects.get(id = data['subject'])
                group.subject =subject
            except Subject.DoesNotExist:
                pass
        if 'student' in data:
            for student in data['student']:
                try:
                    student = Student.objects.get(id = student['id'])
                    group.student.add(student)
                    
                except Student.DoesNotExist:
                    pass
        group.save()
        serializer  = GroupSerializer(group)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def update(self, request, *args, **kwargs):
        data = request.data
        group_object = self.get_object()
        if 'subject' in data:
            try:
                subject = Subject.objects.get(id = data['subject'])
                group_object.subject =subject
            except Subject.DoesNotExist:
                pass
        if 'student' in data:
            for student in data['student']:
                try:
                    student = Student.objects.get(id = student['id'])
                    group_object.student.add(student)
                    
                except Student.DoesNotExist:
                    pass
        group_object.name = data.get('name',group_object.name)
        group_object.save()
        # serializer  = GroupSerializer(group_object)
        return Response(group_object,status=status.HTTP_201_CREATED)
    def partial_update(self, request, *args, **kwargs):
        return self.update( request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        data = request.data
        group_object = self.get_object()
        if 'id' in data:
            group_object.delete()
        if 'student' in data:
            for student in data['student']:
                try:
                    student = Student.objects.get(id = student['id'])
                    group_object.student.remove(student)
                except Student.DoesNotExist:
                    pass
        group_object.name = data.get('name',group_object.name)
        group_object.save()
        return Response({'status':'deleted'})