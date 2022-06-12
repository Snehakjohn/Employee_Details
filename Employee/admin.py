from django.contrib import admin
from .models import Employe

class EmployeAdmin(admin.ModelAdmin):
	list_display = ('name','image')

# Register your models here.
admin.site.register(Employe,EmployeAdmin)