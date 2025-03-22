from django.contrib import admin
from .models import Book, Translator, Genre, Rating


# Register your models here.

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0


class GenreAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class BookAdmin(admin.ModelAdmin):
    exclude = ["added_by_user"]
    inlines = [RatingInline, ]
    list_filter = ('available_for_reading', )

    def save_model(self, request, obj, form, change):
        obj.added_by_user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)


    def has_change_permission(self, request, obj=None):
        if request.user == Book.added_by_user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user == Book.added_by_user:
            return True
        return False

admin.site.register(Book, BookAdmin)
admin.site.register(Translator)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Rating)
