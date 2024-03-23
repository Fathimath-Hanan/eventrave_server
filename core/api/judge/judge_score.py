
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import EventRegistration, JudgeScore



class JudgeScoreListCreateAPIView(APIView):


    def post(self, request, *args, **kwargs):
        event_registration_id = request.data.get('event_registration')
        score = request.data.get('score')
        judge = request.user
        comment = request.data.get('comment')
        try:
            event_registration = EventRegistration.objects.get(id=event_registration_id)
            existing_score = JudgeScore.objects.filter(event_registration=event_registration, judge=judge).first()
            if existing_score:
                existing_score.score = score
                existing_score.comment = comment
                existing_score.save()
            else:
                score_obj = JudgeScore.objects.create(
                    event_registration=event_registration,
                    judge=judge,
                    score=score,
                    comment=comment
                )

            return Response({"message": "Score updated successfully"}, status=status.HTTP_200_OK)
        except EventRegistration.DoesNotExist:
            return Response({"message": "Event registration not found"}, status=status.HTTP_404_NOT_FOUND)