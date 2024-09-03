from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'count', 'display_authors')
    list_filter = ('id', 'name', 'authors')

    def display_authors(self, obj):
        """Display authors as a comma-separated list."""
        return ", ".join(author.name for author in obj.authors.all())  # Adjust based on your Author model's name field

    display_authors.short_description = 'Authors'

admin.site.register(Book, BookAdmin)