from django.contrib import admin
from .models import Person, Property


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'full_name', 'caseNumber', 'sex',
                    'date', 'national_id', 'job', 'approvedPrice', 'commitmentPrice', 'typeBail', 'firstBail',
                    'secondBail', 'expireDate',
                    'clearedStatus', 'clearedDate', 'receivedDocument', 'affidavitStatus', 'office']
    list_per_page = 20
    list_filter = ['office', 'type', 'sex']
    search_fields = (
        "national_id",
        "full_name",
        "id",
        "caseNumber",
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Property)
