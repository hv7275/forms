from django.contrib import admin
from .models import ChaiVarity, ChaiReciews, Store, ChaiCertificate


class ChaiReviwsInline(admin.TabularInline):
    model = ChaiReciews
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'chai_type', 'created_at')
    inlines = [ChaiReviwsInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'locations')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'cerficate_number')

admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
