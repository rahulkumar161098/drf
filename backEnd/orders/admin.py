from django.contrib import admin
from .models import Orders

# Register your models here.
@admin.register(Orders)
class OrderAdminView(admin.ModelAdmin):
    list_display=['customer', 'size', 'quantity', 'created_at']
    list_filter=['size', 'status']