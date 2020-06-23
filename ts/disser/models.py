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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name_e


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


class TechnicalNozzle(models.Model):
    name = models.CharField(verbose_name='Наименование оснастки', max_length=256)
    var_list = (
        ('tipe1','Тип 1'),
        ('tipe2', 'Тип 2'),
        ('tipe3', 'Тип 3'),
        ('tipe4', 'Тип 4'),
        ('tipe5', 'Тип 5'),
        ('tipe6', 'Тип 6'),
        ('tipe7', 'Тип 7'),
    )
    nozzle_tipe = models.CharField(max_length=40, verbose_name='Тип оснастки', choices=var_list)
    count_entity = models.CharField(verbose_name='Гнездность', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Техническая оснастка '
        verbose_name_plural = 'Техническая оснастка'

    def __str__(self):
        return self.name


class OperationEquipment(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='equipment_operation', verbose_name='Оборудование')
    technical_nozzle = models.ForeignKey('TechnicalNozzle', on_delete=models.CASCADE, related_name='nozzle_operation', verbose_name='Техническая оснастка')
    operating_mode = models.CharField(verbose_name='Режим работы', max_length=256)
    note = models.CharField(verbose_name='Примечание', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Оборудование операции'
        verbose_name_plural = 'Оборудование операции'


class StageTP(models.Model):
    name_tp = models.CharField(verbose_name='Наименование стадии', max_length=256)
    note = models.CharField(verbose_name='Примечание', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Стадия Технологического процесса'
        verbose_name_plural = 'Стадии Технологического процесса'

    def __str__(self):
        return self.name_tp


class Operations(models.Model):
    stage_tp = models.ForeignKey('StageTP', on_delete=models.CASCADE, related_name='operations', verbose_name='Стадия ТП')
    operation_equipment = models.ForeignKey('OperationEquipment', on_delete=models.CASCADE, related_name='equipment_operation', verbose_name='Оборудование для операции')
    name = models.CharField(verbose_name='Наименование операции', max_length=256)
    mode = models.CharField(verbose_name='Режим', max_length=256)
    property = models.CharField(verbose_name='Характеристика', max_length=256)
    parameter_name = models.CharField(verbose_name='Наименование параметра', max_length=256)
    measure_unit = models.CharField(verbose_name='Единицы измерения', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return self.name


class Material(models.Model):
    commodities = models.CharField(verbose_name='Вид сырья', max_length=256)
    raw_material_brand = models.CharField(verbose_name='Марка сырья', max_length=256)
    material = models.CharField(verbose_name='Материал', max_length=256)
    name = models.CharField(verbose_name='Наименование сырья', max_length=256)
    price = models.CharField(verbose_name='Цена за килограмм', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Сырье'
        verbose_name_plural = 'Сырье'

    def __str__(self):
        return self.name


class Product(models.Model):
    material = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='product', verbose_name='Материал')
    var_list = (
        ('color1', 'Цвет 1'),
        ('color2', 'Цвет 2'),
        ('color3', 'Цвет 3'),
        ('color4', 'Цвет 4'),
        ('color5', 'Цвет 5'),
        ('color6', 'Цвет 6'),
        ('color7', 'Цвет 7'),
    )
    var_list_tipe = (
        ('1', 'Таз'),
        ('2', 'Ведро'),
        ('3', 'Тип 3'),
        ('4', 'Тип 4'),
        ('5', 'Тип 5'),
        ('6', 'Тип 6'),
        ('7', 'Тип 7'),
    )

    color = models.CharField(verbose_name='Материал', max_length=256, choices=var_list)
    product_tipe = models.CharField(verbose_name='Материал', max_length=256, choices=var_list_tipe)
    name = models.CharField(verbose_name='Наименование изделия', max_length=256)
    nomenclature = models.CharField(verbose_name='Номенклатурный номер изделия', max_length=256)
    form = models.CharField(verbose_name='Тип формы', max_length=256)
    weight = models.CharField(verbose_name='Вес отливки (граммы)', max_length=256)
    net_weight = models.CharField(verbose_name='Чистый вес (граммы)', max_length=256)
    consumption_rate = models.CharField(verbose_name='Норма расхода (граммы)', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'

    def __str__(self):
        return self.name


class TechnologicalMap(models.Model):
    product = models.ForeignKey('Material', on_delete=models.CASCADE, related_name='map', verbose_name='Изделие')
    date = models.DateField()
    number = models.CharField(verbose_name='Номер карты', max_length=256)
    note = models.CharField(verbose_name='Примечание', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Технологическая карта'
        verbose_name_plural = 'Технологические карты'

    def __str__(self):
        return self.number


class PositionTP(models.Model):
    tm = models.ForeignKey('TechnologicalMap', on_delete=models.CASCADE, related_name='position', verbose_name='Технологическая карта')
    stage_tp = models.ForeignKey('StageTP', on_delete=models.CASCADE, related_name='position', verbose_name='Стадия Технологического Процесса')
    normative_value = models.CharField(verbose_name='Нормативное значение', max_length=256)
    note = models.CharField(verbose_name='Примечание', max_length=256)

    class Meta:
        """перевод для админпанели"""
        verbose_name = 'Позиция Технологической карты'
        verbose_name_plural = 'Позиция Технологической карты'
