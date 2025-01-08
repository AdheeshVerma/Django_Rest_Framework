from django.db import models

# Create your models here.
company_types = (("Tech","Tech"),("Non Tech","Non Tech"),("Parts Manufacturer","Parts Manufacturer"))
class company(models.Model):
    company = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50,choices = company_types)
    created_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
