from django.contrib import admin
from .models import Book, Category, Customer

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'quantity', 'price']
    search_fields = ['name', 'author']
    list_filter = ['price']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name', 'id']
    ordering = ['id']


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
