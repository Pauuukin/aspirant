from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    """Производитель оборудования"""
    name = models.CharField(verbose_name='Название производителя', max_length=120)
    country = models.CharField(verbose_name='Страна', max_length=40)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Equipment(models.Model):
    """Оборудование"""
    manufacture = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='equipment',
                                    verbose_name='Производитель')
    genus = models.CharField(verbose_name='Тип\Вид оборудования', max_length=256)
    name_e = models.CharField(verbose_name='Название оборудования', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудованиe'


class TechnicalParam(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='equipment', verbose_name='Оборудование')
    energy_rate = models.CharField(verbose_name='Затрата энергии в час', max_length=40)
    useful_life = models.CharField(verbose_name='Период полезного использования в годах', max_length=40)
    price = models.CharField(verbose_name='Оптовая цена за единицу', max_length=40)
    norm_repair = models.CharField(verbose_name='Норма межремонтных пробегов', max_length=40)
    downtime_rate = models.CharField(verbose_name='Норма простоев оборудования', max_length=40)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Технические характеристики оборудования '
        verbose_name_plural = 'Технические характеристики оборудования '