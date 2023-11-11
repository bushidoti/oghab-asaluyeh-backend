from django.contrib import admin
from .models import Person, Immovable, Movable


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


class ImmovabledAmin(admin.ModelAdmin):
    list_display = ['id', 'typeEstate', 'name', 'docNumber', 'plate',
                    'address', 'landlord', 'meter', 'location', 'madeOf', 'soldDate', 'buyer',
                    'soldStatus']
    list_per_page = 20
    list_filter = ['typeEstate']
    search_fields = (
        "docNumber",
        "name",
        "address",
        "landlord",
        "plate",
        "madeOf",
        "buyer",
    )


class MovableAdmin(admin.ModelAdmin):
    list_display = ['id', 'typeVehicle', 'name', 'docNumber', 'motorNumber', 'chassisNumber', 'descriptionLocation',
                    'part1plate', 'cityPlate', 'part2plate', 'part3plate',
                    'description', 'owner', 'model', 'location', 'madeOf', 'paperDoc', 'insurancePaper', 'gasCard',
                    'carCard', 'soldDate', 'buyer',
                    'soldStatus']
    list_per_page = 20
    list_filter = ['typeVehicle']
    search_fields = (
        "docNumber",
        "name",
        "paperDoc",
        "carCard",
        "gasCard",
        "insurancePaper",
        "chassisNumber",
        "descriptionLocation",
        "motorNumber",
        "model",
        "owner",
        "plate",
        "madeOf",
        "buyer",
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Immovable, ImmovabledAmin)
admin.site.register(Movable, MovableAdmin)
