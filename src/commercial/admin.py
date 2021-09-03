from django.contrib import admin
# Register your models here.

from .models import CommercialDetails, CommercialAmenity , CommercialManager


admin.site.register(CommercialAmenity)


class ResidentialAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug','locality']

    class Meta:
        model = CommercialDetails

    search_fields = ['title', 'slug' , 'locality']


admin.site.register(CommercialDetails, ResidentialAdmin)
