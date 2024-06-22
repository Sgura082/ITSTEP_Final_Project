from django.db import models

# Create your models here.
class Visitor(models.Model):
    visitor_email = models.EmailField
    visitor_age = models.IntegerField
    visitor_ID = models.CharField(max_length=11)
    visitor_name = models.CharField(max_length=30)
    visitor_last_name = models.CharField(max_length=30)
    date_of_visit = models.DateField
    pass