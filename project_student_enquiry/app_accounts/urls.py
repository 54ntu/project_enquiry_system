from django.urls import path
from app_accounts.views import LoginView,DashboardView,RegistrationView,LogoutView

urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegistrationView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),

]
