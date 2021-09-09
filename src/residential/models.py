from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.forms import ModelForm
from django.urls import reverse
from django.db.models import Q
from queenvillas.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.
proprty_sr = (('sell', 'SELL'), ('rent', 'RENT'), ('pg', 'PG'))
property_type = (
('ap', 'APARTMENT'), ('kothi', 'KOTHI'), ('ih', 'INDEPENDENT HOUSE/VILLA'), ('plot', 'PLOT'), ('flat', 'Flat'),
('sa', 'STUDIO APARTMENT'), ('other', 'OTHER'))
furnish_type = (('furnished', 'FURNISHED'), ('semi', 'SEMI-FURNISHED'), ('un', 'UNFURNISHED'))
av_status = (('uc', 'UNDER CONSTRUCTION'), ('rm', 'READY TO MOVE'))
arrea_units = (('feet', 'sq.ft'), ('yards', 'yards'))
possession_type = (
('ready to move', 'Ready To Move'), ('within 2 months', 'Within 2 Months'), ('within 3 months', 'Within 3 Months'))


class Amenity(models.Model):
    amenity = models.CharField(max_length=500)

    def __str__(self):
        return self.amenity


class OtherRooms(models.Model):
    other_rooms = models.CharField(max_length=500)

    def __str__(self):
        return self.other_rooms


class ResidentialQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)

    def search(self, query1, query2, query3, query4, query5, query6):
        if query5 is None:
            query5 = 0
        if query6 is None:
            query6 = 0
        if query5 == '0':
            lookups = (Q(property_type__icontains=query1) & Q(city__icontains=query2) &
                       Q(locality__icontains=query3)
                       & Q(bedrooms__gte=query4)
                       & Q(expected_price__lte=query6))
        if query6 == '0':
            lookups = (Q(property_type__icontains=query1) & Q(city__icontains=query2) &
                       Q(locality__icontains=query3)
                       & Q(bedrooms__gte=query4)
                       & Q(expected_price__gte=query5))
        if query1 == 'all':
            lookups = (Q(city__icontains=query2) &
                       Q(locality__icontains=query3)
                       & Q(bedrooms__gte=query4)
                       & Q(expected_price__gte=query5) & Q(expected_price__lte=query6))
        else:
            lookups = (Q(property_type__icontains=query1) & Q(city__icontains=query2) &
                       Q(locality__icontains=query3)
                       & Q(bedrooms__gte=query4)
                       & Q(expected_price__gte=query5) & Q(expected_price__lte=query6))

        print("lookup= ", lookups)
        return self.filter(lookups).distinct()

    def filtering(self, filter1):
        return self.active()


class ResidentialManager(models.Manager):
    def get_queryset(self):
        return ResidentialQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query1, query2, query3, query4, query5, query6):
        return self.get_queryset().active().search(query1, query2, query3, query4, query5, query6)

    def filtering(self, filter1):
        return self.get_queryset().active().filter(filter1)


class ResidentialDetails(models.Model):
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    locality = models.CharField(max_length=500)
    sub_locality = models.CharField(max_length=255, null=True, blank=True)
    house_no = models.CharField(max_length=255, null=True, blank=True)
    landmark=models.CharField(max_length=500,null=True,blank=True)
    project_society=models.CharField(max_length=500,null=True,blank=True)
    builtupunits=models.CharField(max_length=25,default='yards')
    builtup_area = models.IntegerField(null=True,blank=True)
    carpet_area=models.IntegerField(null=True,blank=True)
    carpet_units= models.CharField(max_length=25, default='yards')
    dim_length = models.IntegerField(null=True, blank=True)
    dim_breadth = models.IntegerField(null=True, blank=True)
    dimension_units=models.CharField(max_length=25,null=True,blank=True)
    property_floor = models.IntegerField(null=True, blank=True)
    property_on_floor=models.IntegerField(null=True, blank=True)
    possession = models.CharField(max_length=255,default='none')
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    balconies = models.IntegerField(null=True, blank=True)
    otherrooms = models.ManyToManyField('OtherRooms', blank=True)
    # amenities = models.ManyToManyField('Amenity', blank=True)
    #amenities=models.CharField(max_length=500,null=True,blank=True)
    am=models.JSONField(null=True, blank=True)
    furnishing = models.CharField(max_length=255)
    availability = models.CharField(max_length=255, choices=av_status, default='uc')
    parkingspace = models.BooleanField(null=True, blank=True)
    ageofproperty = models.IntegerField(null=True,blank=True)
    house_direction=models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='images/', null=True, blank=True)
    image7 = models.ImageField(upload_to='images/', null=True, blank=True)
    image8 = models.ImageField(upload_to='images/', null=True, blank=True)
    expected_price = models.IntegerField()
    price_per_marla = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    verified=models.BooleanField(default=False)
    is_negotiable=models.BooleanField(default=False)
    includes_registration=models.BooleanField(default=False)
    posted_user=models.CharField(max_length=255,null=True,blank=True)
    user_email=models.EmailField()
    user_contact=models.CharField(max_length=12,null=True,blank=True)
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ResidentialManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("residential:detail", kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title + " by " + self.user.username


# class PropertyImage(models.Model):
#     property = models.ForeignKey(ResidentialDetails, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField()


class PropertyModelForm(ModelForm):
    class Meta:
        model = ResidentialDetails
        exclude = ['user']


#
# class PropertyImageForm(ModelForm):
#     class Meta:
#         model = PropertyImage
#         fields = ['image']
def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciever, sender=ResidentialDetails)
