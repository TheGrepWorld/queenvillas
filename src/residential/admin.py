from django.contrib import admin
# Register your models here.

from .models import ResidentialDetails, OtherRooms, Amenity

# admin.site.register(ResidentialDetails)
admin.site.register(OtherRooms)
admin.site.register(Amenity)


class ResidentialAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = ResidentialDetails

    search_fields = ['title', 'slug', 'amenities__amenity']


admin.site.register(ResidentialDetails, ResidentialAdmin)
