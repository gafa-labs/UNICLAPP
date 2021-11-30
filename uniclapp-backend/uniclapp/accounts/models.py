from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.enums import Choices
from django.db.models.fields import EmailField, related
from django.utils import timezone
from club.enums import DepartmentNames


from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
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


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    full_name = models.CharField(max_length=60)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_club_supervisor = models.BooleanField(default=False)
    #is_verified = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user")
    department = models.CharField(
        max_length=30, choices=DepartmentNames.choices)
    is_club_coordinator = models.BooleanField(default=False)
    is_regular_student = models.BooleanField(default=False)
    student_id = models.CharField(max_length=8, unique=True)
    hes_code = models.CharField(max_length=10, unique=True)
    ge_point = models.IntegerField(default=0)


class ClubCoordinator(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="%(class)s_user")
    club = models.OneToOneField(
        "club.Club", on_delete=models.CASCADE, related_name="responsible_club")


class ClubSupervisor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="%(class)s_user")
    club = models.ForeignKey(
        "club.Club", on_delete=models.SET_NULL, related_name="club", null=True, blank=True)


class PSIScore(models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="psi")
    score = models.FloatField(default=0)
