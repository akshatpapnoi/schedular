from django.urls import path, include
from . import views as api_views
app_name = 'api'

urlpatterns = [
    path('', api_views.ScheduleRudView.as_view(), name='ScheduleRudView'),
]