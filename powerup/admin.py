from django.contrib import admin
from powerup.models.client import Client
from powerup.models.pivot import Pivot
from powerup.models.suprima import Suprima
from powerup.models.alert import Alert
from powerup.models.emergency import Emergency
from powerup.models.reg import REG
from powerup.models.top_up import TopUp
from powerup.models.account import Account


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    pass


class PivotAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    pass


class AlertAdmin(admin.ModelAdmin):
    pass


class EmergencyAdmin(admin.ModelAdmin):
    pass


class RegAdmin(admin.ModelAdmin):
    pass


class SuprimaAdmin(admin.ModelAdmin):
    pass


class TopUpAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Pivot, PivotAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(REG, RegAdmin)
admin.site.register(Suprima, SuprimaAdmin)
admin.site.register(TopUp, TopUpAdmin)
