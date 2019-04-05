from django.urls import path
from account import views as account_views

app_name = 'account'

urlpatterns = [
    path('register/', account_views.register, name='register'),
    path('login/', account_views.user_login, name='login'),
    path('logout/', account_views.user_logout, name='logout'),
]