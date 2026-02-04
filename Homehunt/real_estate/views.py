from django.shortcuts import render, get_object_or_404
from .models import Property


# Create your views here.
def index(request):
    properties = Property.objects.all()
    return render(request, "index.html", {"properties": properties})


def property_detail(request, pk):
    prop = get_object_or_404(Property, pk=pk)
    return render(request, "app/property_detail.html", {"property": prop})
