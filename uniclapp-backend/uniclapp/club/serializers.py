from rest_framework import serializers
from club.models import Club, ClubFollowing


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["id", "name", "about", "rate",
                  "category", "number_of_followers", ]


class BasicClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["id", "name", "rate", "category", "number_of_followers", ]


class ClubFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubFollowing
        fields = "__all__"


class ClubLeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["name", "category", "number_of_followers", "rate",
                  "number_of_events", "number_of_total_participants", "rate"]


class ClubProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["about", "category"]
