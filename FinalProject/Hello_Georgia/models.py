from django.db import models

# Create your models here.


class Guides(models.Model):
    guide_ID = models.CharField(max_length=11)
    guide_name = models.CharField(max_length=30)
    guide_last_name = models.CharField(max_length=30)
    guide_mobiluri = models.CharField(max_length=9)

    def __str__(self):
        return (f"ID: {self.guide_ID} / Name: {self.guide_name} / Lastname: {self.guide_last_name} "
                f"/ Mob: {self.guide_mobiluri}")




class Regions(models.Model):
    name = models.CharField(max_length=30)
    number_of_tours = models.IntegerField()

class Tours(models.Model):
    tour_name = models.CharField(max_length=30)
    tour_region = models.ManyToManyField(Regions)
    tour_length_days = models.IntegerField()
    tour_guide = models.ManyToManyField(Guides)
    tour_start_date = models.DateField()
    tour_max_visitorN = models.IntegerField()
    tour_current_visitorN = models.IntegerField()
    tour_free_spots = models.IntegerField()
    def __str__(self):
        return (f"Name: {self.tour_name} / Guide: {self.tour_guide} / Lenght: {self.tour_length_days} / Free spots: {self.tour_free_spots} / Visitors on tour: {self.tour_current_visitorN}")
class Visitor(models.Model):
    visitor_age = models.IntegerField
    visitor_ID = models.CharField(max_length=11)
    visitor_name = models.CharField(max_length=30)
    visitor_last_name = models.CharField(max_length=30)
    date_of_visit = models.DateField
    chosen_tour = models.ManyToManyField(Tours)
    visitor_mobiluri = models.CharField(max_length=9)
    def __str__(self):
        return (f"ID: {self.visitor_ID} / Name: {self.visitor_name} / Lastname: {self.visitor_last_name} "
                f"/ Mob: {self.visitor_mobiluri}")