from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('delete-account/confirm/', views.delete_account_confirm, name='delete_account_confirm'),
    path('delete-account/', views.delete_account, name='delete_account'),
]