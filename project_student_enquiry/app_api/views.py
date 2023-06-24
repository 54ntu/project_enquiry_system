from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from app_api.serializers import CourseSerializer,StudentSerializer
from app_courses.models import courseModel
from app_students.models import studentModel


# Create your views here.
class courseApiView(APIView):
    def get(self,request):
        course_obj = courseModel.objects.all()

        #serializing model object
        serializer =CourseSerializer(course_obj)

        #returning api response with serialize object
        return Response(serializer.data)

    def post(self,request):
        pass

