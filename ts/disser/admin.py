from django.contrib import admin
from .models import *

# Register your models here.


class ManufacturerInline(admin.TabularInline):
    model = Equipment
    can_delete = False
    verbose_name_plural = 'Оборудование'


class ManufacturerAdmin(admin.ModelAdmin):
    model = Manufacturer
    inlines = (ManufacturerInline, )


class MaterialMixInline(admin.TabularInline):
    model = CompositeMixture.composite_mixture.through
    can_delete = False
    extra = 1


@admin.register(CompositeMixture)
class CompositeMixtureAdmin(admin.ModelAdmin):
    """Регистрация модели для композитных смесей"""
    inlines = (MaterialMixInline,)


@admin.register(MaterialMix)
class CompositeMixtureAdmin(admin.ModelAdmin):
    """Регистрация модели для композитных смесей"""
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрация модели для изделий"""
    list_display = ('nomenclature', 'name', 'net_weight', 'product_tipe',)
    extra = 2


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """Регистрация модели для оборудования"""
    list_display = ('manufacture', 'genus', 'name_e', )
    extra = 2


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """Регистрация модели для Material"""
    list_display = ('name', 'commodities', 'raw_material_brand', 'type', 'PTR')
    extra = 2


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(TechnicalParam)
admin.site.register(TechnicalNozzle)
admin.site.register(OperationEquipment)
admin.site.register(StageTP)
admin.site.register(Operations)
admin.site.register(TechnologicalMap)
admin.site.register(PositionTP)


