from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from club.models import Club, ClubFollowing
from club.serializers import ClubSerializer
from club import utils
from club.serializers import BasicClubSerializer, ClubFollowingSerializer, ClubLeaderBoardSerializer
from accounts.serializers import BoardMemberSerializer
from accounts.models import BoardMember


class ClubListAPIView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    lookup_field = 'pk'


class ClubExploreAPIView(generics.RetrieveAPIView):
    serializer_class = BasicClubSerializer
    queryset = Club.objects.all()

    def get(self, request):
        response_data = {}
        user = request.user
        if user:
            student = user.student
            if student:
                clubs = self.get_queryset()
                serializer = self.get_serializer(clubs, many=True)
                data = serializer.data
                following_clubs = utils.get_following_club_list(student.id)
                response_data["following_clubs"] = following_clubs
                response_data["all_clubs"] = data
                return Response(response_data)
            else:
                return ValidationError({"student": "student does not exists!"})
        return ValidationError({"user": "user does not exists!"})


class ClubFollowingsAPIView(generics.RetrieveAPIView):
    serializer_class = BasicClubSerializer
    queryset = Club.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                following_clubs = utils.get_following_club_list(student.id)
                queryset = Club.objects.filter(id__in=following_clubs)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)


class ClubFollowingsFollowAPIView(generics.RetrieveAPIView):
    serializer_class = ClubFollowingSerializer
    queryset = Club.objects.all()

    def get(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                club = Club.objects.get(id=pk)
                if not ClubFollowing.objects.filter(student=student, club=club).exists():
                    club_following = utils.follow_club(student.id, club.id)
                    serializer = ClubFollowingSerializer(club_following)
                    return Response(serializer.data)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ClubFollowingsUnfollowAPIView(generics.RetrieveAPIView):
    serializer_class = ClubFollowingSerializer
    queryset = Club.objects.all()

    def get(self, request, pk):
        user = request.user
        if user:
            student = user.student
            if student:
                club = Club.objects.get(id=pk)
                if ClubFollowing.objects.filter(student=student, club=club).exists():
                    utils.unfollow_club(student.id, club.id)
                    return Response(status=status.HTTP_200_OK)
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LeaderBoardAPIView(generics.ListAPIView):
    serializer_class = ClubLeaderBoardSerializer
    queryset = Club.objects.all()


class ClubBoardMemberListAPIView(generics.ListAPIView):
    serializer_class = BoardMemberSerializer
    queryset = BoardMember.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                boardchairman = student.board_chairman
                if boardchairman:
                    club = boardchairman.club
                    board_members = club.boardmembers.all()
                    serializer = self.get_serializer(board_members, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
