from django.shortcuts import render
from evaluation.models import Evaluation
from rest_framework import generics
from evaluation.serializers import EvaluationSerializer
from event.models import Event
from rest_framework.response import Response
from rest_framework import status


class EvaluationCreateAPIView(generics.CreateAPIView):
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.all()

    def post(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                event = Event.objects.get(pk=pk)
                if event:
                    if not Evaluation.objects.filter(student=student, event=event).exists():
                        data = request.data
                        data["event"] = event.id
                        data["student"] = student.id
                        serializer = self.get_serializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)

                    return Response(status=status.HTTP_400_BAD_REQUEST)


class EvaluationListAPIView(generics.ListAPIView):
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.all()
