from django.shortcuts import render,HttpResponse
from rest_framework.serializers import Serializer
from studentapp.models import Student, StudentGrades,StudentMarks
from rest_framework import viewsets
from rest_framework import permissions
from studentapp.serializers import StudentSerializer,StudentMarksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.

@api_view(['GET','POST'])
def StudentViewSet(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def AddMarks(request):
    if request.method == 'GET':
        studentmarks = StudentMarks.objects.all()
        serializer = StudentMarksSerializer(studentmarks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentMarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Student_results(request):
    if request.method == 'GET':
        total_students = StudentMarks.objects.all().count()

        # Grade_A_students=StudentMarks.objects.filter(studentgrade='1').values('student','marks','studentgrade')
        Grade_A_students=StudentMarks.objects.filter(studentgrade='1').count()
        Grade_B_students=StudentMarks.objects.filter(studentgrade='2').count()
        Grade_C_students=StudentMarks.objects.filter(studentgrade='3').count()
        Grade_D_students=StudentMarks.objects.filter(studentgrade='4').count()
        Grade_E_students=StudentMarks.objects.filter(studentgrade='5').count()
        Grade_F_students=StudentMarks.objects.filter(studentgrade='6').count()

        distinction_students= (Grade_A_students/total_students)*100
        firstclass_students= (Grade_B_students+Grade_C_students)/total_students*100
        pass_percentage=((total_students- Grade_F_students)/total_students)*100
        return Response({
            'Total Number of Students': total_students,
            'Total number of Students with Grade A': Grade_A_students,
            'Total number of Students with Grade B': Grade_B_students,
            'Total number of Students with Grade C': Grade_C_students,
            'Total number of Students with Grade D': Grade_D_students,
            'Total number of Students with Grade E': Grade_E_students,
            'Total number of Students with Grade F': Grade_F_students,
            'Total No of Students in Distinction (%)':distinction_students,
            'Total No of Students in First Class (%)':firstclass_students,
            'Total No of Students Pass Percentage (%)':pass_percentage,
        })

class Results(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'studentresults.html'

    def get(self, request):
        total_students = StudentMarks.objects.all().count()

        # Grade_A_students=StudentMarks.objects.filter(studentgrade='1').values('student','marks','studentgrade')
        Grade_A_students=StudentMarks.objects.filter(studentgrade='1').count()
        Grade_B_students=StudentMarks.objects.filter(studentgrade='2').count()
        Grade_C_students=StudentMarks.objects.filter(studentgrade='3').count()
        Grade_D_students=StudentMarks.objects.filter(studentgrade='4').count()
        Grade_E_students=StudentMarks.objects.filter(studentgrade='5').count()
        Grade_F_students=StudentMarks.objects.filter(studentgrade='6').count()

        distinction_students= (Grade_A_students/total_students)*100
        firstclass_students= (Grade_B_students+Grade_C_students)/total_students*100
        pass_percentage=((total_students- Grade_F_students)/total_students)*100
        return Response({
            'total_students': total_students,
            'Grade_A_students': Grade_A_students,
            'Grade_B_students': Grade_B_students,
            'Grade_C_students': Grade_C_students,
            'Grade_D_students': Grade_D_students,
            'Grade_E_students': Grade_E_students,
            'Grade_F_students': Grade_F_students,
            'distinction_students':distinction_students,
            'firstclass_students':firstclass_students,
            'pass_percentage':pass_percentage,
        })






