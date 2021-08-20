from django.urls import path
from . import views

urlpatterns=[
    path('student/',views.StudentViewSet,name="student"),
    path('student/add-mark/',views.AddMarks,name='addmarks'),
    path('students/results/',views.Student_results,name='student_results'),
    path('results/',views.Results.as_view(),name='results')
]