from rest_framework import generics
from main.models import Schedule

from .serializers import ScheduleSerializer

class ScheduleRudView(generics.ListCreateAPIView):


	serializer_class = ScheduleSerializer

	def get_queryset(self):
		return Schedule.objects.filter(user = self.request.user)
