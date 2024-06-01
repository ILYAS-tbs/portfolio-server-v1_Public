from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Links)
admin.site.register(DeployedLinks)
admin.site.register(Tech)
admin.site.register(Image)
admin.site.register(Video)