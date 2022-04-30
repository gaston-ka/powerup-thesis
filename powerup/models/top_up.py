from django.db import models
import uuid
from django.db.models.deletion import SET_NULL
from powerup.models.account import Account
from powerup.models.pivot import Pivot


class TopUp(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    account = models.ForeignKey(Account, on_delete=SET_NULL, null=True, help_text="Related Momo Account")
    balance = models.FloatField(blank=False, null=False, help_text="UNIT", default=0.0)
    new_unit = models.FloatField(blank=False, null=False, help_text="UNIT", default=0.0)
    pivot_number = models.ForeignKey(Pivot, blank=False, null=True, on_delete=SET_NULL,  help_text="Pivot Number")
    encr_message = models.CharField(blank=False, null=False, max_length=255, help_text="Encrypted Message")
    top_up_date = models.DateTimeField(blank=False, null=False, auto_now_add=True, help_text="TopUP Date")

    class Meta:
        db_table = 'top_up'
        verbose_name = 'TopUp'
        verbose_name_plural = 'TopUp'