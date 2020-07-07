from django.contrib import admin

from .models import data
from .models import search
# Register your models here.
admin.site.register(data)
admin.site.register(search)
