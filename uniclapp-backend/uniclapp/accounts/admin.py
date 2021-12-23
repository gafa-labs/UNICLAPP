from django.contrib import admin
from accounts import models


admin.site.register(models.Student)
admin.site.register(models.ClubAdvisor)
admin.site.register(models.BoardMember)
admin.site.register(models.BoardChairman)
admin.site.register(models.OEM)
admin.site.register(models.User)
