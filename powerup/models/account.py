from django.db import models
import uuid
from django.db.models.deletion import SET_NULL
from powerup.models.client import Client
from powerup.models.suprima import Suprima


class Account(models.Model):
    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    client = models.ForeignKey(Client, on_delete=SET_NULL, null=True, help_text="Client")
    phone = models.CharField(blank=False, null=False, max_length=10, help_text="Phone number", unique=True)
    suprima = models.ForeignKey(Suprima, on_delete=SET_NULL, null=True, help_text="Suprima")
    balance = models.FloatField(blank=False, null=False, help_text="UNIT", default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date created")
    REQUIRED_FIELDS = ["phone"]

    class Meta:
        db_table = "account"
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
