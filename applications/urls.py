from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]