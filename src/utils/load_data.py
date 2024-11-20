import csv
from pollution_data.models import AirQualityRecord

def load_data_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            AirQualityRecord.objects.create(
                date=row['date'],
                aqi=int(row['aqi']),
                pm25=float(row['pm25']),
                pm10=float(row['pm10']),
                source=row['source']
            )