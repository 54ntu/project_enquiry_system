from django.shortcuts import render,redirect
from app_students.models import studentModel
from app_students.forms import StudentCreateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def student_create(request):
    form= StudentCreateForm()
    context={"form": form}


    if request.method == "POST":
        std = StudentCreateForm(request.POST, request.FILES) ##### here we use  object of form
        if std.is_valid():
            std.save()
            return redirect("student-index")
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
        data =StudentCreateForm(data=request.POST,instance=instance)
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


