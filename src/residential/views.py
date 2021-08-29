from django.http.response import Http404
from django.shortcuts import render
from .models import PropertyModelForm
from .models import ResidentialDetails
from django.views.generic import ListView, DetailView
from .forms import Filterform
from django.views.generic.edit import FormView
from django.db.models import Q


# from analytics.mixins import ObjectViewdMixin


def add_property(request):
    property_form = PropertyModelForm()
    return render(request, 'add_prop.html', {'form': property_form})


image_list = []


def add_image(request):
    if request.METHOD == 'POST':
        image_list.append(request.POST['image'])


def ResidentialListView(request):
    bedrooms = request.GET.get('bedrooms')
    print(bedrooms)
    filter_form = Filterform
    price = request.GET.get('price')
    selected_bhk = 0
    if bedrooms:
        print("in if bedromms")
        object_list = ResidentialDetails.objects.filter(bedrooms__iexact=bedrooms)
    if price:
        print("in if price")
        if price=='3000000':
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price)
        if price== '5000000':
            print(price)
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(expected_price__gte=3000000)
        if price == '10000000':
            print(price)
            object_list = ResidentialDetails.objects.filter(expected_price__lte=price).filter(expected_price__gte=5000000)
        if price == '100000001':
            object_list = ResidentialDetails.objects.filter(expected_price__gte='10000000')
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


# class ResidentialListView(ListView):
#     template_name = "residentials/list.html"
#     paginate_by = 24
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ResidentialListView, self).get_context_data(*args, **kwargs)
#         request = self.request
#         return context
#
#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return ResidentialDetails.objects.all()


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
