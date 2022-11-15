from django.contrib import admin
import DeliveryFood.models as models
# Register your models here.

admin.site.register(models.Foods)
admin.site.register(models.Orders)
admin.site.register(models.Categories)
admin.site.register(models.Adress)