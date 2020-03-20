from django.db import models

class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    zip_code = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
