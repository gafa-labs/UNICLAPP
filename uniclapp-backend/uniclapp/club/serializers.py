from rest_framework import serializers
from club.models import Club, ClubFollowing


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["id", "name", "about", "rate",
                  "category", "number_of_followers", ]


class ClubFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["name", "rate", "category", "number_of_followers", ]
