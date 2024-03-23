
from account.models import CustomUser

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Event(models.Model):
    class EventStatus(models.TextChoices):
        UPCOMING = 'upcoming', _('Upcoming')
        ONGOING = 'ongoing', _('Ongoing')
        COMPLETED = 'completed', _('Completed')
        CANCELLED = 'cancelled', _('Cancelled')
        
    name = models.CharField(max_length=255)
    is_onstage = models.BooleanField(default=True, help_text='True for onstage events, False for offstage events.')
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/', )
    is_group_event = models.BooleanField(default=False)
    group_limit = models.PositiveIntegerField(null=True, blank=True, help_text='Limit for group participation if this is a group event.')
    judges = models.ManyToManyField(CustomUser, related_name='events_as_judge', blank=True)
    status = models.CharField(max_length=20, choices=EventStatus.choices, default=EventStatus.UPCOMING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['datetime']


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='event_registrations')
    members = models.ManyToManyField(CustomUser, related_name='group_registrations',blank=True, help_text='Members of the group if this is a group event.')
    jest_number = models.PositiveIntegerField( blank=True, help_text='Jest number for the member in the event.')
    position = models.PositiveIntegerField(null=True, blank=True, help_text='Position secured by the participant in the event.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.email} registered for {self.event.name}'




class JudgeScore(models.Model):
    event_registration = models.ForeignKey(EventRegistration, on_delete=models.CASCADE, related_name='judge_scores')
    judge = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='judged_scores')
    score = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.judge.email} scored {self.score} for {self.event_registration}'

    class Meta:
        unique_together = ('event_registration', 'judge')



class Certificate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='certificates')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='certificates')
    pdf = models.FileField(upload_to='certificates/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Certificate for {self.user.email} in {self.event.name}'
