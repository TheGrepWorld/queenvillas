from django.contrib import admin
# Register your models here.

from .models import ResidentialDetails, propertyPossesion, OtherRooms

admin.site.register(ResidentialDetails)
admin.site.register(propertyPossesion)
admin.site.register(OtherRooms)


# class PropertyImageInline(admin.TabularInline):
#     model = PropertyImage
#     extra = 3
#
#
# class PropertyAdmin(admin.ModelAdmin):
#     inlines = [PropertyImageInline, ]


# admin.site.register(ResidentialDetails, PropertyAdmin)
