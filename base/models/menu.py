# app base/models/menu.py
from django.db import models

class Menu(models.Model):
    nama = models.CharField(max_length=100)
    urutan = models.PositiveIntegerField(default=0)
    ikon = models.CharField(max_length=100, blank=True)  # optional, untuk ikon di UI

    def __str__(self):
        return self.nama
