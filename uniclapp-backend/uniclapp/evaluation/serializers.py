from rest_framework import serializers
from evaluation.models import Evaluation
from event.serializers import EventSerializer


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"


class AdvancedEvaluationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Evaluation
        fields = "__all__"
