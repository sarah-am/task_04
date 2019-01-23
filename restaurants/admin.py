from django.contrib import admin
from .models import Restaurant

# Register your models here.

# class Fields(admin.ModelAdmin):
# 	fields = ['opening_time', 'closing_time']

# class FieldsAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

class FieldsAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'description','opening_time', 'closing_time')

admin.site.register(Restaurant, FieldsAdmin)