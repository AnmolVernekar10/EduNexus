from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Files)
admin.site.register(file_name_against_keyword)
admin.site.register(keyword_against_file_name)