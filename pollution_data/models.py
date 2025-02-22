from django.db import models

class AirQualityRecord(models.Model):
     date = models.DateField()
     aqi = models.IntegerField()
     pm25 = models.FloatField()
     pm10 = models.FloatField()
     source = models.CharField(max_length=255)

     def __str__(self):
          return f"{self.date}: AQI {self.aqi}"

