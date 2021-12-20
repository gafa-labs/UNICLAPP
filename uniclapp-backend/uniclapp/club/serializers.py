from rest_framework import serializers
from uniclapp.club.models import Club, Classroom, Event, Building, Evaluation


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        exclude = ['logo']


class ClassroomSerializer(serializers.ModelSerializer):
    pass


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    pass


class BuildingSerializer(serializers.ModelSerializer):
    pass
