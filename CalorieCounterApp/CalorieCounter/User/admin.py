from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserNewActivity)
admin.site.register(UserNewItem)
admin.site.register(FoodConsumption)
admin.site.register(ActivityPerformed)


