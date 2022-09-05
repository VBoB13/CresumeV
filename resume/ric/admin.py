from django.contrib import admin

from .models import Education, Subject, Experience, Location

# Register your models here.
admin.site.register(Education)
admin.site.register(Subject)
admin.site.register(Experience)
admin.site.register(Location)
