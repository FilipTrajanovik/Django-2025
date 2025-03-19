from django.contrib import admin
from market.models import Market, MarketProduct, ContactInformation, Product, Employee


# Register your models here.

class ProductInline(admin.TabularInline):
    model = MarketProduct
    extra = 0


class MarketAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ["added_by"]

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return False
        if request.user == obj.added_by:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False
        if request.user == obj.added_by:
            return True
        return False


admin.site.register(Market, MarketAdmin)
admin.site.register(ContactInformation)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product)
