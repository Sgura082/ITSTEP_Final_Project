from django.contrib import admin
from .models import Visitor,Guides,Tours
# Register your models here.


admin.site.register(Tours)
admin.site.register(Guides)
admin.site.register(Visitor)