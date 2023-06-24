from django.urls import path
from app_api.views import courseApiView

urlpatterns = [
    path('courses/',courseApiView.as_view())
    
]
