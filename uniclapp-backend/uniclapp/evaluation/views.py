from django.shortcuts import render
from evaluation.models import Evaluation
from rest_framework import generics
from evaluation.serializers import EvaluationSerializer


class EvaluationCreateAPIView(generics.CreateAPIView):
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.all()
