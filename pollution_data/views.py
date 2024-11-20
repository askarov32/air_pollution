from django.shortcuts import render
from .models import AirQualityRecord

def index(request):
     records = AirQualityRecord.objects.all()

     return render(request, 'pollition_data/index.html', {'records': records})