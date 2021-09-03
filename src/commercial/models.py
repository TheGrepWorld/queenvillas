from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from queenvillas.utils import unique_slug_generator
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL

proprty_sr = (('sell', 'SELL'), ('rent', 'RENT'))
property_type = (('booth', 'Booth'), ('showroom', 'Showroom'), ('cp', 'Commercial Plot'))
av_status = (('uc', 'UNDER CONSTRUCTION'), ('rm', 'READY TO MOVE'))
arrea_units = (('feet', 'sq.ft'), ('yards', 'yards'))
possession_type = (
    ('ready to move', 'Ready To Move'), ('within 2 months', 'Within 2 Months'), ('within 3 months', 'Within 3 Months'))
furnish_type = (('furnished', 'FURNISHED'), ('semi', 'SEMI-FURNISHED'), ('un', 'UNFURNISHED'))


class CommercialAmenity(models.Model):
    amenities = models.CharField(max_length=500)

    def __str__(self):
        return self.amenities


class CommercialQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)

#     def search(self, query1, query2, query3, query4, query5, query6):
#         if query5 is None:
#             query5 = 0
#         if query6 is None:
#             query6 = 0
#         if query5 == '0':
#             lookups = (Q(property_type__icontains=query1) & Q(city__icontains=query2) &
#                        Q(locality__icontains=query3)
#                        & Q(bedrooms__gte=query4)
#                        & Q(expected_price__lte=query6))
#         if query6 == '0':
#             lookups = (Q(property_type__icontains=query1) & Q(city__icontains=query2) &
#                        Q(locality__icontains=query3)
#                        & Q(bedrooms__gte=query4)
#                        & Q(expected_price__gte=query5))
#         if query1 == 'all':
#             lookups = (Q(city__icontains=query2) &
#                        Q(locality__icontains=query3)
#                        & Q(bedrooms__gte=query4)
#                        & Q(expected_price__gte=query5) & Q(expected_price__lte=query6))
#         else:
#             lookups = (Q(property_type__icontains=query1) & Q(city__icontains=query2) &
#                        Q(locality__icontains=query3)
#                        & Q(bedrooms__gte=query4)
#                        & Q(expected_price__gte=query5) & Q(expected_price__lte=query6))
#
#         print("lookup= ", lookups)
#         return self.filter(lookups).distinct()
#
#     def filtering(self, filter1):
#         return self.active()
#

class CommercialManager(models.Manager):
    def get_queryset(self):
        return CommercialQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id)
    #     if qs.count() == 1:
    #         return qs.first()
    #     return None
    #
    # def search(self, query1, query2, query3, query4, query5, query6):
    #     return self.get_queryset().active().search(query1, query2, query3, query4, query5, query6)
    #
    # def filtering(self, filter1):
    #     return self.get_queryset().active().filter(filter1)


# Create your models here.
class CommercialDetails(models.Model):
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=255, choices=proprty_sr)
    property_type = models.CharField(max_length=255, choices=property_type)
    city = models.CharField(max_length=255)
    locality = models.CharField(max_length=500)
    sub_locality = models.CharField(max_length=255, null=True, blank=True)
    shop_no = models.CharField(max_length=255, null=True, blank=True)
    area = models.IntegerField()
    ar_units = models.CharField(max_length=25, choices=arrea_units, default='yards')
    dim_length = models.IntegerField(null=True, blank=True)
    dim_breadth = models.IntegerField(null=True, blank=True)
    floors = models.IntegerField()
    possession = models.CharField(max_length=255, choices=possession_type, default='none')
    amenities = models.ManyToManyField('CommercialAmenity', blank=True)
    furnishing = models.CharField(max_length=255, choices=furnish_type)
    availability = models.CharField(max_length=255, choices=av_status, default='uc')
    parkingspace = models.BooleanField(null=True, blank=True)
    ageofproperty = models.IntegerField()
    main_image = models.ImageField(upload_to='images/', null=True, blank=True)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='images/', null=True, blank=True)
    image7 = models.ImageField(upload_to='images/', null=True, blank=True)
    image8 = models.ImageField(upload_to='images/', null=True, blank=True)
    expected_price = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(User,
                             default=1,
                             null=True,
                             on_delete=models.SET_NULL
                             )
    timestamp = models.DateTimeField(auto_now_add=True)
    is_commercial = models.BooleanField(default=True)
    objects = CommercialManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("commercial:detail", kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title + " by " + self.user.username


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciever, sender=CommercialDetails)
