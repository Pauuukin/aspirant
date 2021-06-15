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




admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Equipment)
admin.site.register(TechnicalParam)
admin.site.register(TechnicalNozzle)
admin.site.register(OperationEquipment)
admin.site.register(StageTP)
admin.site.register(Operations)
admin.site.register(Material)
admin.site.register(Product)
admin.site.register(TechnologicalMap)
admin.site.register(PositionTP)


