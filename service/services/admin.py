from django.contrib import admin
from services.models import Service, Plan, Subscription

# Register your models here.
admin.site.register(Plan)
admin.site.register(Service)
admin.site.register(Subscription)
