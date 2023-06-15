from django.contrib import admin
from app_students.models import studentModel

# Register your models here.

class studentModelAdmin(admin.ModelAdmin): # this  line of code is for displaying the table with column names
    list_display = ("first_name","last_name","contact","course")
    search_fields = ("first_name","contact")
    list_filter = ("course",)





admin.site.register(studentModel,studentModelAdmin)
