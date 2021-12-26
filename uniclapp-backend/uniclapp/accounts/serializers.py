from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Student, OEM, BoardMember
from club.serializers import ClubSerializer
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "full_name"]


class OEMSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', "full_name", ]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        if not User.objects.filter(email=self.validated_data["email"], password=self.validated_data["password"]).exists():
            user = User.objects.create_user(
                email=self.validated_data["email"], password=self.validated_data["password"],)
            user.full_name = self.validated_data["full_name"]
            user.save()
            oem = OEM.objects.create(user=user)
            return user
        return ValidationError()


class StudentRegisterSerializer(serializers.ModelSerializer):
    studentid = serializers.CharField(max_length=8)
    department = serializers.CharField(max_length=5)

    class Meta:
        model = User
        fields = ['email', 'password', "full_name",
                  "studentid", "department"]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        student_id = self.validated_data["studentid"]
        if self.validate_student_id(student_id):
            student = Student.objects.filter(student_id=student_id).first()
            if student:
                raise serializers.ValidationError(
                    {"student_id": f"{student_id} already exists."})
            else:
                user = User.objects.create_user(
                    email=self.validated_data["email"],
                    password=self.validated_data["password"],
                )
                user.is_student = True
                user.full_name = self.validated_data["full_name"]
                user.save()
                student = Student.objects.create(user=user, department=self.validated_data["department"],
                                                 student_id=self.validated_data["studentid"],)

                return user
        return None

    def validate_student_id(self, id):
        if len(id) != 8:
            raise serializers.ValidationError(
                {"student_id": {"student_id must be 8 digits!"}})
        if not id.isdecimal():
            raise serializers.ValidationError(
                {"student_id": {"student_id must contain only numbers!"}})
        return True


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["student_id", "department", "hes_code", "user"]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]


class BoardMemberSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    club = ClubSerializer(read_only=True)

    class Meta:
        model = BoardMember
        fields = "__all__"


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
