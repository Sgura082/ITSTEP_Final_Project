from django.contrib import admin
from .models import Visitor,Guide,Tour,Region
# Register your models here.


admin.site.register(Tour)
admin.site.register(Guide)
admin.site.register(Visitor)
admin.site.register(Region)