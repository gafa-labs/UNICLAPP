from django.urls import path
from evaluation.views import EvaluationCreateAPIView, EvaluationListAPIView

urlpatterns = [
    path('evaluations/<int:pk>/make-evaluation/',
         EvaluationCreateAPIView.as_view(), name='make-evaluation'),
    path('evaluations/', EvaluationListAPIView.as_view(), name='evaluations'),
]
