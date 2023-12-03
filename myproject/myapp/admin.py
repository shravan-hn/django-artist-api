from django.contrib import admin

# Register your models here.
from .models import Artist, Work
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')  

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('link', 'work_type') 
