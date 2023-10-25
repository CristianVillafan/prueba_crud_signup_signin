from django.contrib import admin
from .models import Orders

class ordersAdmin(admin.ModelAdmin):
    readonly_fields = ("price", "create", )


# Register your models here.
admin.site.register(Orders, ordersAdmin)