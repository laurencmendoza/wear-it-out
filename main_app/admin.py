from django.contrib import admin
# import your models here
from .models import ClothingItem, Color, Tag, Outfit, Photo, OutfitPhoto, Date

# Register your models here.
admin.site.register(ClothingItem)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Outfit)
admin.site.register(Photo)
admin.site.register(OutfitPhoto)
admin.site.register(Date)