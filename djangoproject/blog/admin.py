from django.contrib import admin
from .models import Form
# Register your models here.

class Formadmin(admin.ModelAdmin):
    list_display = [ 
        'name', 'number', 'time', 'choice'
    ]


admin.site.register(Form, Formadmin)
