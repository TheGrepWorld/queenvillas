from django.conf import settings
from django.db import models
from django.forms import ModelForm

User = settings.AUTH_USER_MODEL

# Create your models here.
proprty_sr = (('sell', 'SELL'), ('rent', 'RENT'), ('pg', 'PG'))
property_type = (('ap', 'APARTMENT'), ('kothi', 'KOTHI'), ('ih', 'INDEPENDENT HOUSE/VILLA'), ('plot', 'PLOT'),
                 ('sa', 'STUDIO APARTMENT'), ('other', 'OTHER'))
furnish_type = (('furnished', 'FURNISHED'), ('semi', 'SEMI-FURNISHED'), ('un', 'UNFURNISHED'))
av_status = (('uc', 'UNDER CONSTRUCTION'), ('rm', 'READY TO MOVE'))
arrea_units = (('feet', 'sq.ft'), ('yards', 'yards'))


class propertyPossesion(models.Model):
    possession_type = models.CharField(max_length=500)

    def __str__(self):
        return self.possession_type


class OtherRooms(models.Model):
    other_rooms = models.CharField(max_length=500)

    def __str__(self):
        return self.other_rooms


class ResidentialDetails(models.Model):
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=255, choices=proprty_sr)
    property_type = models.CharField(max_length=255, choices=property_type)
    city = models.CharField(max_length=255)
    locality = models.CharField(max_length=500)
    sub_locality = models.CharField(max_length=255, null=True, blank=True)
    house_no = models.CharField(max_length=255, null=True, blank=True)
    area = models.IntegerField()
    ar_units = models.CharField(max_length=25, choices=arrea_units, default='yards')
    dim_length = models.IntegerField(null=True, blank=True)
    dim_breadth = models.IntegerField(null=True, blank=True)
    floors = models.IntegerField()
    possession = models.OneToOneField('propertyPossesion', on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    balconies = models.IntegerField(null=True, blank=True)
    otherrooms = models.ManyToManyField('OtherRooms', blank=True)
    furnishing = models.CharField(max_length=255, choices=furnish_type)
    availability = models.CharField(max_length=255, choices=av_status, default='uc')
    parkingspace = models.BooleanField(null=True, blank=True)
    ageofproperty = models.IntegerField()
    image = models.ImageField(upload_to='images/' ,null=True, blank=True)
    expected_price = models.IntegerField()
    price_per_marla = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )

    def __str__(self):
        return self.title + " by " + self.user.username


class PropertyImage(models.Model):
    property = models.ForeignKey(ResidentialDetails, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()


class PropertyModelForm(ModelForm):
    class Meta:
        model = ResidentialDetails
        exclude = ['user']


class PropertyImageForm(ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']
