from rest_framework import serializers
from main.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        exclude = []