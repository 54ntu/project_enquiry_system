from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.student_create,name='student-create'),
    path('list/',views.student_index,name='student-index'),
    path('edit/<int:id>/',views.student_edit,name='student-edit'),
    path('show/<int:id>/',views.student_show,name='student-show'),
    path('update/',views.student_update,name='student-update'),
    path('delete/<int:id>',views.student_delete,name='student-delete')



]
