from django.http.response import Http404
from django.shortcuts import render
from .models import PropertyModelForm
from .models import ResidentialDetails
from django.views.generic import ListView, DetailView
# from analytics.mixins import ObjectViewdMixin



def add_property(request):
    property_form = PropertyModelForm()
    return render(request, 'add_prop.html', {'form': property_form})


image_list = []


def add_image(request):
    if request.METHOD == 'POST':
        image_list.append(request.POST['image'])


class ResidentialListView(ListView):
    template_name = "residentials/list.html"
    paginate_by = 24

    def get_context_data(self,*args,**kwargs):
        context = super(ResidentialListView, self).get_context_data(*args,**kwargs)
        request = self.request
        return context

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return ResidentialDetails.objects.all()


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


