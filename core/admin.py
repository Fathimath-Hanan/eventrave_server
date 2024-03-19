from django.contrib import admin

from core.models import Certificate, EventRegistration,JudgeScore,Event
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    pass

@admin.register(JudgeScore)
class JudgeScoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "EventRave"
admin.site.site_title = "EventRave"