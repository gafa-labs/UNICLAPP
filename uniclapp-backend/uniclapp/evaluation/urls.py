from django.urls import path
from evaluation.views import EvaluationCreateAPIView

urlpatterns = [
    path('club/<int:club_id>/<int:event_id>/',
         EvaluationCreateAPIView.as_view(), name='evaluation'),
]
