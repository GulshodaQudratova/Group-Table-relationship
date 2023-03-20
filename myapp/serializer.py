from rest_framework import serializers
from .models import *
class GroupSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    count = serializers.SerializerMethodField(read_only = True)
    def get_count(self,obj):
        return obj.studentscount
    # student = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = '__all__'
        # read_only_fields = ['id']
        depth = 1
class StudentSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    group_count = serializers.SerializerMethodField(read_only = True)
    def get_group_count(self,obj):
        return obj.groupscount
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['id']
class SubjectSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True,read_only=True)
    count = serializers.SerializerMethodField(read_only = True)
    def get_count(self,obj):
        return obj.groupscount
    class Meta:
        model = Subject
        fields = '__all__'
        # read_only_fields = ['id']
