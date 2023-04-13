from django.db import models
# Orijinal url'yi, kısaltılmış url'yi ve ziyaretçi sayısını tutan bir veritabanı oluşturduk.
class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=6)
    visit_count = models.PositiveIntegerField(default=0)