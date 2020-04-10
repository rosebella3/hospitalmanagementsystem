from django.contrib import admin
from .models import Patient, Bills, Room, LabReport
# Register your models here.

admin.site.register(Patient)
admin.site.register(Bills)
admin.site.register(Room)
admin.site.register(LabReport)
