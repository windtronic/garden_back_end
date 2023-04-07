from django.db import models




class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.EmailField()
    password = models.CharField(max_length = 200)


class Calendar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='calenders')
    frost_dates = models.DateField(null=True, blank=True)
    plant_dates = models.DateField(null=True, blank=True)
    harvest_times = models.DateTimeField(null=True, blank=True)
    fertilize_dates = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True)

    

# class Garden(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     # add any other fields you need for the garden, such as location, size, etc.

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    name = models.CharField(max_length=100)
    

class PlantListing(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plant_listings')
    name = models.CharField(max_length=100)
    row_spacing = models.CharField(max_length=100)
    seed_depth = models.CharField(null=True, blank=True, max_length=100)
    sunlight_needs = models.CharField(max_length=200, null=True, blank=True)
    season = models.CharField(null=True, blank=True, max_length=200)
    water_needs = models.TextField(blank=True)
    frost_tolerance = models.TextField(blank=True)
    germination_time = models.CharField(null=True, blank=True, max_length=100)
    harvest_times = models.CharField(null=True, blank=True, max_length=100)
    grow_from_seed = models.BooleanField(null=True, blank=True)
    grow_from_transplant = models.BooleanField(null=True, blank=True)
    plant_needs_fertilization = models.BooleanField(null=True, blank=True)
    date_to_plant = models.TextField(blank=True)

    
  