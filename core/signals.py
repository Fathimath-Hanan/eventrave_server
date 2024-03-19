import os
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.db.models import Sum, F
from core.utils.certificate_generator import CertificateGenerator

from core.models import Certificate, Event, EventRegistration, JudgeScore

@receiver(post_save, sender=JudgeScore)
def update_event_registration_position(sender, instance, created, **kwargs):
    if created:
        event_registration = instance.event_registration
        total_score = event_registration.judge_scores.aggregate(total_score=Sum('score'))['total_score']
        if total_score is not None:
            event_registrations = EventRegistration.objects.filter(event=event_registration.event)\
                                                             .annotate(total_score=Sum('judge_scores__score'))\
                                                             .order_by('-total_score', '-created_at')
            for index, reg in enumerate(event_registrations):
                reg.position = index + 1
                reg.save()

@receiver(pre_save, sender=EventRegistration)
def set_jest_number(sender, instance, **kwargs):
    if not instance.jest_number:
        event_registrations_count = EventRegistration.objects.filter(event=instance.event).count()
        instance.jest_number = event_registrations_count + 1
        
        




@receiver(pre_save, sender=Event)
def generate_certificates(sender, instance, **kwargs):
    if instance.status == Event.EventStatus.COMPLETED and instance.pk:
        previous_instance = Event.objects.get(pk=instance.pk)
        if previous_instance.status != Event.EventStatus.COMPLETED:
            # Event status changed from ongoing to completed
            registrations = EventRegistration.objects.filter(event=instance)
            positions = [1, 2, 3]
            for position in positions:
                winner = registrations.filter(position=position).first()
                if winner:
                    # Generate certificate for winner
                    position_str = 'First' if position == 1 else 'Second' if position == 2 else 'Third'
                    certificate_data = {
                        'id': winner.student.id,
                        'event': instance.name,
                        'name': winner.student.get_full_name(),
                        'position': position_str
                    }
                    certificate_path = CertificateGenerator.generate(
                        data=certificate_data,
                        certemplate= "cert.pdf",horz= 350, vert=270,fontname= "certfont.ttf",fontsize= 30, 
                           fontcolor="#000000")
                    if certificate_path:
                        Certificate.objects.create(
                            event=instance,
                            user=winner.student,
                            pdf=certificate_path
                        )
