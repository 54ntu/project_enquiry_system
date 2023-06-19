from django.shortcuts import render,redirect
from app_students.models import studentModel,courseModel
from app_students.forms import StudentCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login')
def student_create(request):
    form= StudentCreateForm()
    context={"form": form}
    if request.method == "POST":
        # user= user.objects.get(id=request.user.id)

        # std = StudentCreateForm(request.POST, request.FILES) ##### here we use  object of form
        course =courseModel.objects.get(id=request.POST.get('course'))
        std_odj = studentModel()
        std_odj.first_name = request.POST.get('first_name')
        std_odj.middle_name = request.POST.get('middle_name')
        std_odj.last_name = request.POST.get('last_name')
        std_odj.email =request.POST.get('email')
        std_odj.contact = request.POST.get('contact')
        std_odj.address= request.POST.get('address')
        std_odj.created_at=request.POST.get('created_at')
        std_odj.current_degree=request.POST.get('current_degree')
        std_odj.course=course
        std_odj.profile_img = request.POST.get('profile_img')
        std_odj.user= request.user
        std_odj.save()
        # if std.is_valid():
        #     std.save()
        #     return redirect("student-index")
        return redirect("student-create")
    return render(request,"students/create.html",context)


@login_required(login_url='/login')
def student_index(request):
    students = studentModel.objects.all()
    context = {
        "students" :students,
        "title":"SES | List",
        "body_content":"here the student details "
    }
    return render(request,"students/index.html",context)


@login_required(login_url='/login')
def student_edit(request,id):
    students=studentModel.objects.get(id=id)
    context={"students":students}
    return render(request, 'students/edit.html',context)

@login_required(login_url='/login')
def student_show(request,id):
    students = studentModel.objects.get(id=id)
    context ={"students":students}
    return render(request,'students/show.html',context)


def student_update(request):
    if request.method == "POST":
        instance = studentModel.objects.get(id=request.POST.get('id'))
        data =StudentCreateForm(data=request.POST,instance=instance,files=request.FILES)
        if data.is_valid:
            data.save()
            return redirect('student-index')
        return redirect('student-index')
    return redirect('student-index')


@login_required(login_url='/login')
def student_delete(request,id):
    students=studentModel.objects.get(id=id)
    students.delete()
    return redirect('student-index')


