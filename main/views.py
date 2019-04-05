from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import generics

from .models import Schedule
# # Create your views here.

def home(request):
	return render(request, template_name='main/home.html')

@login_required(login_url=reverse_lazy('account:login'))
def dashboard(request):
	schedules = Schedule.objects.filter(user = request.user).filter(start_time__gte = timezone.now()).order_by('start_time')
	archives = Schedule.objects.filter(user = request.user).filter(start_time__lte = timezone.now()).order_by('-start_time')
	context = {
		'schedules': schedules,
		'archives': archives,
	}

	return render(request, template_name='main/dashboard.html', context=context)

