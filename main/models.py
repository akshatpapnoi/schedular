from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class Schedule(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, null=True)
	start_time = models.DateTimeField(_("Starting Time"))
	end_time = models.DateTimeField(_("Ending Time"), blank=True, null=True)
	description = models.CharField(max_length=200, blank=True, null=True)
	is_complete = models.BooleanField(default=False)

	def clean(self, *args, **kwargs):

		super(Schedule, self).clean(*args, **kwargs)

		if self.start_time < timezone.now():
			raise ValidationError('Start time must be later than current time.')

		if self.end_time < self.start_time:
			raise ValidationError('End time must be later than Start time.')

	def __str__(self):
		return str(self.user.username) + '--->' + str(self.start_time)

