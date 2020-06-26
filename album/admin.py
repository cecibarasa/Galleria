from django.contrib import admin
from .models import Photographer,Photos,Location,Category,tag

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Photos,PhotosAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(tag)
