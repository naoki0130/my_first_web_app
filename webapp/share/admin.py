from django.contrib import admin
from . import models

@admin.register(models.ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    pass