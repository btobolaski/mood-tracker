from django.contrib import admin

from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ["date"]


# Register your models here.

admin.site.register(Record, RecordAdmin)
