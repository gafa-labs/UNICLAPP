from django.core.exceptions import ValidationError
from club.models import Club, ClubFollowing
from accounts.models import Student


def follow_club(student_id, club_id):
    student = Student.objects.get(id=student_id)
    club = Club.objects.get(id=club_id)
    if student and club:
        club_following = ClubFollowing.objects.create(
            student=student, club=club)
        return club_following
    return ValidationError()


def get_following_club_list(student_id):
    student = Student.objects.get(id=student_id)
    if student:
        all_followings = ClubFollowing.objects.filter(student=student).all()
        all_followings = list(all_followings)
        clubs = []
        for instance in all_followings:
            clubs.append(instance.club.id)
        return clubs
