# app base/models/menu_access.py
from django.db import models
from django.conf import settings

from base.models import Menu, SubMenu, OPD

class Role(models.Model):
    """
    Jika kamu ingin memisahkan role dari Group bawaan Django.
    Kalau tidak, bisa diabaikan dan pakai Group saja.
    """
    nama = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama
    
class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, null=True, blank=True)
    
    # Menentukan akses CRUD
    can_create = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_view = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['role', 'menu', 'submenu'], name='unique_role_menu_submenu')
        ]
        
    def __str__(self):
        return f"Role {self.role} - Akses ke {self.menu} > {self.submenu or '-'}"
    
class MenuAccess(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    opd = models.ForeignKey(OPD, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'role', 'opd'], name='unique_menu_access')
        ]
        

    def __str__(self):
        return f"Akses: {self.user or self.group } -> {self.role} untuk opd {self.opd}"
