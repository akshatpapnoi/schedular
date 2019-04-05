from django.urls import path, include
from main import views as main_views

app_name = 'main'

urlpatterns = [
    path('', main_views.home, name='home'),
    path('dashboard', main_views.dashboard, name='dashboard'),
]