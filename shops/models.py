from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Название")
    city = models.ForeignKey('City', null = True, blank=True, default='', on_delete=models.CASCADE, verbose_name='Город', related_name='shop' )
    street = models.ForeignKey('Street', null = True, blank=True, default='', on_delete=models.CASCADE, verbose_name='Улица', related_name='shop' )
    house = models.IntegerField(null = True, blank=True, verbose_name="Номер дома")
    opening_time = models.TimeField(verbose_name="Время Открытия", blank=True, null=True)
    closing_time = models.TimeField(verbose_name="Время Закрытия", blank=True, null=True)
   
    class Meta:
        verbose_name = u'Магазин'
        verbose_name_plural = u'Магазины'

    def __str__(self):
        return str(self.name)

class City(models.Model):
    name = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Название")
   
    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'

    def __str__(self):
        return str(self.name)

class Street(models.Model):
    name = models.CharField(max_length = 1000, null = True, blank=True, verbose_name="Название")
    city = models.ForeignKey('City', null = True, blank=True, default='', on_delete=models.CASCADE, verbose_name='Город', related_name='street' )
   
    class Meta:
        verbose_name = u'Улица'
        verbose_name_plural = u'Улицы'

    def __str__(self):
        return str(self.name)
