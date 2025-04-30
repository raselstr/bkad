from django.db import models
from .menu import Menu


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='submenus', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    urutan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.menu.nama} > {self.nama}"
