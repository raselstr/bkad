from django.db import models
from django.contrib.auth.models import User
from base.models import OPD
from base.models.menu_access import Role

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    opd = models.ForeignKey(OPD, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
