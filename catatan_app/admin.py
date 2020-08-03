from django.contrib import admin
from .models import Catatan
# Register your models here.

class CatatanAdmin(admin.ModelAdmin):
    fieldsets = [
        ('KONTEN (TANGGAL OTOMATIS DIISI)', {'fields': ['judul', 'isi']}),
    ]

    list_display = ('judul', 'tanggal')

admin.site.register(Catatan, CatatanAdmin)

# user = sendiri
# pass = passsementara