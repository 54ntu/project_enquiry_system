from django.urls import path
from app_api.views import courseApiView,StudentApiview,CourseApiIdView

urlpatterns = [
    path('courses/',courseApiView.as_view()),
    path('courses/<int:id>/',CourseApiIdView.as_view()),

    path('students/',StudentApiview.as_view()),
    
]
