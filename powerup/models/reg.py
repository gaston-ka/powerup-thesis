from django.db import models
import uuid
from django.db.models.deletion import SET_NULL
from powerup.models.client import Client
from powerup.models.pivot import Pivot


class REG(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    client = models.ForeignKey(Client, on_delete=SET_NULL, null=True, help_text="Related Client")
    location = models.CharField(blank=False, null=False, max_length=255, help_text="Location")
    phone = models.CharField(blank=False, null=False, help_text="REG Phone number", max_length=13)
    pivot = models.ForeignKey(Pivot, on_delete=SET_NULL, null=True, help_text="Related Pivot")
    REQUIRED_FIELDS = ["phone"]

    class Meta:
        db_table = 'reg'
        verbose_name = 'REG'
        verbose_name_plural = 'REG'
        unique_together = (("client_id", "pivot_id"),)
