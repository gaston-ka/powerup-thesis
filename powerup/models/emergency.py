from django.db import models
import uuid
from django.db.models.deletion import SET_NULL
from powerup.models.pivot import Pivot


class Emergency(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    pivot_number = models.ForeignKey(Pivot, on_delete=SET_NULL, null=True, help_text="Related Pivot")
    message = models.CharField(blank=False, null=False, max_length=255, help_text="Message Code")
    reg_tel = models.IntegerField(blank=False, null=False, default=0, help_text="REG Phone number")

    class Meta:
        db_table = 'Emergency'
        verbose_name = 'Emergency'
        verbose_name_plural = 'Emergencies'