from django.db import models
import uuid
from django.db.models.deletion import SET_NULL
from powerup.models.pivot import Pivot


class Alert(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    pivot_number = models.ForeignKey(Pivot, on_delete=SET_NULL, null=True, help_text="Related Pivot")
    message = models.CharField(blank=False, null=False, max_length=255, help_text="Message")
    REQUIRED_FIELDS = ["pivot_number"]

    class Meta:
        db_table = 'Alert'
        verbose_name = 'Alert'
        verbose_name_plural = 'Alert'
