from rest_framework import serializers
from club.models import Club, ClubFollowing


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ["name", "about", "rate",
                  "category", "number_of_followers", ]


class ClubFollowingSerializer(serializers.ModelSerializer):
    is_follow = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = ["name", "rate", "category", "number_of_followers", ]

    def get_is_follow(self, student):
        return student.followers.all()
