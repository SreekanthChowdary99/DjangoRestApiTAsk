from rest_framework import serializers
from studentapp.models import Student,StudentMarks,StudentGrades

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StudentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = "__all__"