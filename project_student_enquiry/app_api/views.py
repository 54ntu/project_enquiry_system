from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from app_api.serializers import CourseSerializer,StudentSerializer,Userserializer
from app_courses.models import courseModel
from app_students.models import studentModel
from django.contrib.auth.models import User


# Create your views here.
class courseApiView(APIView):
    def get(self,request):
        course_obj = courseModel.objects.all()

        #serializing model object
        serializer =CourseSerializer(course_obj, many=True)

        #returning api response with serialize object
        return Response(serializer.data)

    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class CourseApiIdView(APIView):
    def get_object(self,id):
        try:
            course_obj = courseModel.objects.get(id=id)
            return course_obj
        except courseModel.DoesNotExist:
            return None

    def get(self,request,id):
        instance= self.get_object(id)
        if instance is None:
            return Response({"error":"No data found"})
        serializer =CourseSerializer(instance)
        return Response(serializer.data)

    def put(self,request,id):
         instance = self.get_object(id)
         if instance is None:
             return Response({"error":"no data found"})
         serializer = CourseSerializer(instance=instance)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors)
    
    
    def delete(self,request,id):
        instance = self.get_object(id)
        if instance is None:
            return Response({"errors":"no data is found"})
        instance.delete()
        return Response({'message':'data deleted successfully'})

class StudentApiview(APIView):
    def get(self,request):
        std_obj = studentModel.objects.all()

        #serializing model object
        serializer= StudentSerializer(std_obj,many=True)

        # user = User.objects.all()
        # serializer =Userserializer(user,many=True)
        return Response(serializer.data)


        # returning api response with serialize object
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    