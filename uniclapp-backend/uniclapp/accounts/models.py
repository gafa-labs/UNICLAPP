from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from accounts import enums
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        self.email_validator(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def email_validator(self, email):
        if email:
            print(email)
            format = email.split("@",)[1]
            if format == "ug.bilkent.edu.tr":
                self.model(is_student=True)
            elif format == "oem.bilkent.edu.tr":
                self.model(is_oem=True)
            else:
                self.model(is_club_advisor=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    full_name = models.CharField(max_length=60)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_club_advisor = models.BooleanField(default=False)
    is_board_member = models.BooleanField(default=False)
    is_board_chairman = models.BooleanField(default=False)
    is_oem = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student")
    department = models.TextField(choices=enums.DepartmentNames.choices)
    student_id = models.CharField(max_length=8, unique=True)
    hes_code = models.CharField(
        max_length=12, unique=True, blank=True, null=True)
    ge_point = models.IntegerField(default=0)

    def __str__(self):
        return self.user.full_name


class BoardMember(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="boardmember")
    club = models.ForeignKey(
        "club.Club", on_delete=models.CASCADE, related_name="boardmembers")

    def __str__(self):
        return self.student.user.full_name


class BoardChairman(models.Model):
    boardmember = models.OneToOneField(
        BoardMember, on_delete=models.CASCADE, related_name="board_chairman")
    club = models.OneToOneField(
        "club.Club", on_delete=models.CASCADE, related_name="chairman", null=True, blank=True)

    def __str__(self):
        return self.boardmember.student.user.full_name


class ClubAdvisor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="club_advisor")
    club = models.OneToOneField(
        "club.Club", on_delete=models.CASCADE, related_name="club")

    def __str__(self):
        return self.user.full_name


class OEM(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="oem")

    def __str__(self):
        return self.user.full_name


class PSIScore(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="psi")
    score = models.FloatField(default=0)

    def __str__(self):
        return f'{self.student.user.full_name} - {self.score}'

    def update_score(self):
        pass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
