from django.db import models

class OPD(models.Model):
    kode_opd = models.CharField(max_length=20, unique=True)
    nama_opd = models.CharField(max_length=255)

    class Meta:
        verbose_name = "OPD"
        verbose_name_plural = "OPD"
        ordering = ['nama_opd']

    def __str__(self):
        return f"{self.kode_opd} - {self.nama_opd}"
