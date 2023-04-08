from django.db import models




class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name


class Calendar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='calenders')
    frost_dates = models.CharField(max_length=100, default='no frost date')
    plant_dates = models.CharField(max_length=100, default='no plant date')
    harvest_times = models.CharField(max_length=100, default='no harvest time')
    fertilize_dates = models.CharField(max_length=100, default=None)
    comments = models.TextField(default='')

    def __str__(self):
        return self.user
    

# class Garden(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     # add any other fields you need for the garden, such as location, size, etc.

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plants')
    name = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.name
    

class PlantListing(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plant_listings')
    name = models.CharField(max_length=100, default='')
    row_spacing = models.CharField(max_length=100, default='')
    seed_depth = models.CharField(max_length=100, default='')
    sunlight_needs = models.CharField(max_length=200, default='')
    season = models.CharField(max_length=200, default='')
    water_needs = models.CharField(max_length=200, default='')
    frost_tolerance = models.CharField(max_length=200, default='')
    germination_time = models.CharField(max_length=100, default='')
    harvest_times = models.CharField(max_length=100, default='')
    grow_from_seed = models.BooleanField(default=False)
    grow_from_transplant = models.BooleanField(default=False)
    plant_needs_fertilization = models.BooleanField(default=False)
    date_to_plant = models.CharField(max_length=200, default='')


    def __str__(self):
        return self.name
  