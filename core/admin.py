from django.contrib import admin

from core.models import Certificate, EventJudges, Participant,Event,Score, Judge

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    pass

@admin.register(EventJudges)
class EventJudgesAdmin(admin.ModelAdmin):
    pass




admin.site.site_header = "EventRave"
admin.site.site_title = "EventRave"