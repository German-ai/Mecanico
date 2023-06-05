from django.db import models

class Car (models.Model):
    vin_number =
model.ChartFiled(max_length=17)
    make =
models.CharFiled(max_lenght=50)
    model =
models.CharField(max_length=50)
#Add more fileds as needed
class MaintenanceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    odometer = models.IntegerField()
    # Add more fields as needed
    
