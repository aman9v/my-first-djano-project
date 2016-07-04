from django.contrib import admin
from .models import Book, Library


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_pub', 'library_id',)


class BookInline(admin.StackedInline):
    model = Book


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
     inlines = [
        BookInline,
     ]

