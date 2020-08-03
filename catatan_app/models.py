from django.db import models

# Create your models here.

class Catatan(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal = models.DateField(auto_now_add=True)