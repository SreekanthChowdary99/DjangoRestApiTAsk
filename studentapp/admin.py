from django.contrib import admin
from .models import Student,StudentMarks,StudentGrades

# Register your models here.

class Ids(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Student,Ids)
admin.site.register(StudentMarks,Ids)
admin.site.register(StudentGrades,Ids)