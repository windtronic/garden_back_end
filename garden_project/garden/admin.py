from django.contrib import admin

from django.contrib import admin
from .models import User, Calendar, Plant, PlantListing
admin.site.register(User)
admin.site.register(Calendar)
admin.site.register(Plant)
admin.site.register(PlantListing)

