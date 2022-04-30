from django.db import models
import uuid


class Pivot(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    number = models.CharField(blank=False, null=False, max_length=255, help_text="Plot Number")
    unit = models.IntegerField(blank=False, null=False, default=0, help_text="Pivot Number")
    longitude = models.FloatField(blank=False, null=False, default=0.0, help_text="Longitude")
    latitude = models.FloatField(blank=False, null=False, default=0.0, help_text="Latitude")

    class Meta:
        db_table = 'Pivot'
        verbose_name = 'Pivot'
        verbose_name_plural = 'Pivots'