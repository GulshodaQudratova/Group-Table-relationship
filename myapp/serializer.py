from rest_framework import serializers
from .models import *
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # my_choices = serializers.MultipleChoiceField(choice = day)
    student = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ['id']
class StudentSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']
class SubjectSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True,read_only=True)
    count = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['id']
