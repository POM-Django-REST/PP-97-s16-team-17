from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ('user', 'book', 'created_at', 'end_at')

admin.site.register(Order, OrderAdmin)