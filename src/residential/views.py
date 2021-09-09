import json

from django.http.response import Http404
from django.shortcuts import render
from .models import PropertyModelForm
from .models import ResidentialDetails
from django.views.generic import ListView, DetailView
from .forms import Filterform
from django.views.generic.edit import FormView
from django.db.models import Q


# from analytics.mixins import ObjectViewdMixin
def add_property_data(request):
    if request.method == 'POST':
        rd = ResidentialDetails()
        print("mei andar aagya")
        rd.title = request.POST['title']
        rd.type = request.POST['postType']
        rd.property_type = request.POST['propertyType']
        price = request.POST['sale_price']
        rd.expected_price = int(price.replace(",",""))
        print(price,rd.expected_price)
        rd.descritpion = request.POST['description']
        is_negotiable = request.POST.get('is_negotiable', 'off')
        rd.bedrooms = request.POST['bedrooms']
        rd.city = request.POST['city']
        rd.locality = request.POST['locality']
        rd.sub_locality = request.POST['sublocality']
        rd.house_no = request.POST['houseno']
        rd.project_society = request.POST['projectname']
        rd.landmark = request.POST['landmark']
        rd.builtup_area = request.POST['built-up']
        rd.carpet_area = request.POST['carpet']
        rd.builtupunits = request.POST['builtupunits']
        rd.carpet_units = request.POST['carpetunits']
        rd.dimension_units = request.POST['dim_units']
        rd.dim_length = request.POST['dim_length']
        rd.dim_breadth = request.POST['dim_breadth']
        rd.property_on_floor = request.POST['property_on_floor']
        includes_registration = request.POST.get('includes_registration', 'off')
        rd.total_floors = request.POST['total_floors']
        rd.furnishing = request.POST['furnishing']
        rd.bathrooms = request.POST['bathrooms']
        rd.balconies = request.POST['balconies']
        rd.house_direction = request.POST['house_direction']
        rd.posted_user = request.POST['user_type']
        rd.user_email = request.POST['email_input']
        rd.user_contact = request.POST['phoneno']
        rd.possession = request.POST['posession']
        amenities=request.POST.getlist('amenity_item')
        am_json=json.dumps(amenities)
        rd.am=am_json
        if is_negotiable == 'on':
            rd.is_negotiable = True
        else:
            rd.is_negotiable = False

        if includes_registration == 'on':
            rd.includes_registration = True
        else:
            rd.includes_registration = False

        images = len(request.FILES.getlist('Image'))
        print(amenities)
        if images == 1:
            rd.image = request.FILES.getlist('Image')[0]
        if images == 2:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
        if images == 3:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
            rd.image2 = request.FILES.getlist('Image')[2]
        if images == 4:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
            rd.image2 = request.FILES.getlist('Image')[2]
            rd.image3 = request.FILES.getlist('Image')[3]
        if images == 5:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
            rd.image2 = request.FILES.getlist('Image')[2]
            rd.image3 = request.FILES.getlist('Image')[3]
            rd.image4 = request.FILES.getlist('Image')[4]
        if images == 6:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
            rd.image2 = request.FILES.getlist('Image')[2]
            rd.image3 = request.FILES.getlist('Image')[3]
            rd.image4 = request.FILES.getlist('Image')[4]
            rd.image5 = request.FILES.getlist('Image')[5]
        if images == 7:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
            rd.image2 = request.FILES.getlist('Image')[2]
            rd.image3 = request.FILES.getlist('Image')[3]
            rd.image4 = request.FILES.getlist('Image')[4]
            rd.image5 = request.FILES.getlist('Image')[5]
            rd.image6 = request.FILES.getlist('Image')[6]
        if images == 8:
            rd.image = request.FILES.getlist('Image')[0]
            rd.image1 = request.FILES.getlist('Image')[1]
            rd.image2 = request.FILES.getlist('Image')[2]
            rd.image3 = request.FILES.getlist('Image')[3]
            rd.image4 = request.FILES.getlist('Image')[4]
            rd.image5 = request.FILES.getlist('Image')[5]
            rd.image6 = request.FILES.getlist('Image')[6]
            rd.image7 = request.FILES.getlist('Image')[7]

        rd.save()
        return render(request, 'residentials/added-prop.html')


def add_property(request):
    if request.method == 'GET':
        return render(request, 'residentials/add_prop.html')


def ResidentialListView(request):
    bedrooms = request.GET.get('bedrooms')
    filter_form = Filterform()
    price = request.GET.get('price')
    selected_bhk = 0
    if bedrooms is not None and price is None:
        print("in if bedromms", bedrooms)
        initial_dict = {
            "bhks": bedrooms
        }
        filter_form = Filterform(initial=initial_dict)
        object_list = ResidentialDetails.objects.filter(bedrooms__iexact=bedrooms)

    elif price is not None and bedrooms is None:
        initial_dict = {
            "price": price

        }
        filter_form = Filterform(initial=initial_dict)
        print("in if price")
        if price == '3000000':
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price)
        if price == '5000000':
            print(price)
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=3000000)
        if price == '10000000':
            print(price)
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=5000000)
        if price == '100000001':
            object_list = ResidentialDetails.objects.filter(expected_price__gte='10000000')
    elif price is not None and bedrooms is not None:
        initial_dict = {
            "price": price,
            "bhks": bedrooms

        }
        filter_form = Filterform(initial=initial_dict)
        print("in b and p")
        if price == '3000000':
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(bedrooms__iexact=bedrooms)
        if price == '5000000':
            print(price)
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=3000000).filter(bedrooms__iexact=bedrooms)
        if price == '10000000':
            print(price)
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(
                expected_price__gte=5000000).filter(bedrooms__iexact=bedrooms)
        if price == '100000001':
            object_list = ResidentialDetails.objects.filter(expected_price__gte='10000000').filter(
                bedrooms__iexact=bedrooms)
    else:
        selected_bhk = 0
        print("kuch toh gadbad hai ")
        object_list = ResidentialDetails.objects.all()
    context = {
        "selected_bhk": selected_bhk,
        "object_list": object_list,
        "filter_form": filter_form
    }
    return render(request, "residentials/list.html", context)


def get_filter_data(request):
    queryset = ResidentialDetails.objects.none()
    if request.method == 'GET':
        bhks = request.GET.getlist('bhk')
        print(bhks)
        if bhks is not None:
            for i in bhks:
                queryset |= (ResidentialDetails.objects.all().filter(bedrooms__iexact=i))
    print(queryset)

    context = {
        "data": queryset
    }
    return render(request, "residentials/resfilter.html", context)


class ResidentialDetailSlugView(DetailView):
    queryset = ResidentialDetails.objects.all()
    template_name = "residentials/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ResidentialDetailSlugView, self).get_context_data(*args, **kwargs)
        request = self.request
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = ResidentialDetails.objects.get(slug=slug)
        except ResidentialDetails.DoesNotExist:
            raise Http404("Not Found....")
        except ResidentialDetails.MultipleObjectsReturned:
            qs = ResidentialDetails.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmm.. !")
        return instance
