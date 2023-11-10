from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_form', 'name', 'contractNumber', 'topicContract',
                    'dateContract', 'typeContract', 'durationContract', 'contractPrice', 'prePaidPrice', 'goodPrice',
                    'typeBail1', 'firstBail', 'secondBail', 'commitmentPrice', 'typeBail2', 'firstBail2',
                    'secondBail2', 'clearedStatus', 'clearedDate', 'receivedDocument', 'office']
    list_per_page = 20
    list_filter = ['type_form', 'typeContract']
    search_fields = (
        "id",
        "name",
        "contractNumber",
        "topicContract",
        "typeContract",
    )


admin.site.register(Document, DocumentAdmin)
