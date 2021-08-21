from django.shortcuts import render
from .models import PropertyModelForm, PropertyImageForm
from .models import ResidentialDetails
from django.views.generic import ListView  , DetailView


def add_property(request):
    property_form = PropertyModelForm()
    property_image_form = PropertyImageForm()
    return render(request, 'add_prop.html', {'form': property_form, 'image_form': property_image_form})


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
