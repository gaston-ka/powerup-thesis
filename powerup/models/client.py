from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", "MALE"
        FEMALE = "FEMALE", "FEMALE"
        NONE = "NONE", "NONE"

    id = models.BigAutoField(primary_key=True, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')
    nid = models.CharField(blank=False, max_length=16, help_text="National ID", unique=True, null=False)
    first_name = models.CharField(blank=False, max_length=250, help_text="First Name", null=False)
    last_name = models.CharField(blank=True, max_length=250, help_text="Last Name", null=True)
    phone = models.CharField(blank=False, max_length=16, help_text="Last Name", null=False, unique=True)
    email = models.EmailField(blank=False, max_length=250, help_text="Email", null=False, unique=True)
    address = models.CharField(blank=True, max_length=250, help_text="Address", null=True)
    dob = models.DateField(blank=True, max_length=250, help_text="Date of Birth", null=True)
    gender = models.CharField(blank=True, max_length=250, help_text="Gender", null=True,choices=Gender.choices)
    marital_status = models.CharField(blank=True, max_length=250, help_text="Marital Status", null=True)

    REQUIRED_FIELDS = ['nid', 'first_name', 'phone', 'email']

    class Meta:
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
