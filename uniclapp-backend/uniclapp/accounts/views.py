from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from accounts import serializers
from accounts.serializers import LoginSerializer, StudentRegisterSerializer, OEMSerializer, BoardMemberSerializer
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from accounts import models
from rest_framework.permissions import AllowAny, IsAuthenticated


class StudentRegisterAPIView(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "successfully registered a new student"
            data["email"] = user.email
            data["full_name"] = user.full_name
            token = Token.objects.get_or_create(user=user)[0].key
            data["token"] = token
        else:
            raise ValidationError()
        return Response(data)


class OEMRegisterAPIView(generics.CreateAPIView):
    serializer_class = OEMSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["response"] = "successfully registered a new user"
            data["email"] = user.email
            data["full_name"] = user.full_name
            token = Token.objects.get_or_create(user=user)[0].key
            data["token"] = token
        else:
            raise ValidationError()
        return Response(data)


class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    queryset = models.User.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request):
        data = {}
        request_data = request.data
        email = request_data.get('email', None)
        password = request_data.get('password', None)
        try:
            user = models.User.objects.get(email=email)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=user)[0].key
        if not user.check_password(password):
            raise ValidationError({"message": "Incorrect Login credentials"})
        if user:
            login(request, user)
            data["message"] = "user logged in"
            data["email_address"] = user.email
            response = {"data": data, "token": token}
            return Response(response)
        else:
            raise ValidationError({"400": f'User does not exist'})


class LogoutAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)


class StudentProfileAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def get(self, request):
        user = request.user
        if user:
            student = models.Student.objects.get(user=user)
            serializer = self.get_serializer(student)
            data = serializer.data
            data["name"] = user.full_name
            data["email"] = user.email
            return Response(data)


class PromoteStudentAPIView(generics.CreateAPIView):
    serializer_class = BoardMemberSerializer
    queryset = models.BoardMember.objects.all()

    def post(self, request):
        user = request.user
        if user:
            student = user.student
            if student:
                boardmember = student.boardmember
                if boardmember:
                    club = boardmember.club
                    data = request.data
                    full_name = data["student_name"]
                    student_id = data["student_id"]
                    email = data["email"]
                    user = models.User.objects.get(
                        email=email, full_name=full_name)
                    if user:
                        student = user.student
                        if student:
                            candidate_student = models.Student.objects.get(
                                user=user, student_id=student_id)
                            if student == candidate_student:
                                if not models.BoardMember.objects.filter(student=student, club=club):
                                    boardmember = models.BoardMember.objects.get_or_create(
                                        student=student, club=club)
                                    return Response(status=status.HTTP_201_CREATED)
                        return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


class DemoteStudentAPIView(generics.DestroyAPIView):
    serializer_class = BoardMemberSerializer
    queryset = models.BoardMember.objects.all()
