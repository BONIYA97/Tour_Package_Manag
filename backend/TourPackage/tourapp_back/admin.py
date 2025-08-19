from django.contrib import admin
from .models import Country, City, Package, Schedule, Enquiry,  Banner

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Package)
admin.site.register(Schedule)
admin.site.register(Enquiry)
admin.site.register(Banner)