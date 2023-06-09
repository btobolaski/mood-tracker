from django.contrib import admin

from .models import Record, Tag, Medication, MedicationDosage


class RecordAdmin(admin.ModelAdmin):
    list_display = ["date"]


# Register your models here.

admin.site.register(Record, RecordAdmin)
admin.site.register(Tag)
admin.site.register(Medication)
admin.site.register(MedicationDosage)
