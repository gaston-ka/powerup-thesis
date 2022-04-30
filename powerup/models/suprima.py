from django.db import models
import uuid


class Suprima(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    name = models.CharField(blank=False, null=False, max_length=255, help_text="Name")
    tin = models.CharField(blank=False, null=False, max_length=255, help_text="TIN Number")
    location = models.CharField(blank=False, null=False, max_length=255, help_text="Location")
    unit = models.FloatField(blank=False, null=False, help_text="UNIT", default=0.0)

    class Meta:
        db_table = 'suprima'
        verbose_name = 'suprima'
        verbose_name_plural = 'suprima'
