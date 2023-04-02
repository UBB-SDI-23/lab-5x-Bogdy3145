from django.contrib import admin
from .models import Cars
from .models import Brand
from .models import Customers
from .models import CarOwnership

admin.site.register(Cars)
admin.site.register(Brand)
admin.site.register(Customers)
admin.site.register(CarOwnership)