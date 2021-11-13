from django.contrib import admin
from .models import Book, Category

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'author',
        'published_date',
        'price',
        'category',
        'image',
    )
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
