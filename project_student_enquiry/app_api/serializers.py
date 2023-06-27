from rest_framework import serializers
from app_students.models import studentModel
from app_courses.models import courseModel
from django.contrib.auth.models import User



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id","course_name","course_code")
        model = courseModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields =["id","first_name","middle_name","last_name","email","contact","address","course","current_degree","user"]
        model=studentModel


class Userserializer(serializers.ModelSerializer):
    class Meta:
        fields =['id',"first_name","username"]
        model=User