from django.contrib import admin
# import your models here
from .models import ClothingItem, Color, Tag

# Register your models here.
admin.site.register(ClothingItem)
admin.site.register(Color)
admin.site.register(Tag)