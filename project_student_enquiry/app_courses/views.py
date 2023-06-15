from django.shortcuts import render,redirect
from .forms import CourseCreateForm
from app_courses.models import courseModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
@login_required(login_url='/login')
def course_index(request):
    courses = courseModel.objects.all()
    context={
        "title":"SES | courses",
        "body_content":"here are the courses details",
        "courses" : courses
    }
    return render(request,'courses/index.html',context)

@login_required(login_url='/login')
def course_create(request):
    form = CourseCreateForm()
    context ={"form":form}
    if request.method == "POST":
        #method 1
        # name = request.POST.get("course_name")
        # code= request.POST.get("course_code")
        # obj = courseModel(course_name=name,course_code= code)
        # obj.save()

        # method 2
        obj = courseModel()
        obj.course_name = request.POST.get('course_name')
        obj.course_code = request.POST.get('course_code')
        obj.save()
        messages.success(request,"course added successfully")
        return redirect('course-index')
    return render(request,'courses/create.html',context)

def course_show(request,id):
   course= courseModel.objects.get(id=id)
   context = {"course": course}
   return render(request,'courses/show.html',context)

@login_required(login_url='/login')
def course_edit(request,id):
    course = courseModel.objects.get(id=id)
    context ={"course":course}
    return render(request,'courses/edit.html',context)


@login_required(login_url='/login')
def course_delete(request,id):
    course=courseModel.objects.get(id=id)
    course.delete()
    messages.error(request,"course deleted successfully")
    return redirect('course-index')


def course_update(request):
    if request.method == "POST":
        # instance = courseModel.objects.get(id=request.POST.get('id'))
        data = CourseCreateForm(data=request.POST)
        if data.is_valid():
            data.save()

            return redirect("course-index")
        return redirect("course-index")
    return redirect("course-index")