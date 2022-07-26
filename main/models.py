from django.db import models
from django.utils.translation import gettext_lazy as _


class PopularCarModel(models.Model):
    brand = models.CharField(max_length=50, verbose_name=_('brand'))
    image = models.ImageField(upload_to='popular_car/', verbose_name=_('image'))
    model = models.CharField(max_length=30, verbose_name=_('model'))
    condition = models.CharField(max_length=30, verbose_name=_('condition'))
    year = models.CharField(max_length=4, verbose_name=_('year'))
    motor_type = models.CharField(max_length=30, verbose_name=_('motor type'))
    fuel = models.CharField(max_length=30, verbose_name=_('fuel'))
    price = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_('price'))
    max_speed = models.CharField(max_length=3, verbose_name='maximal speed')
    is_active = models.BooleanField(default=False, blank=True, verbose_name=_('is active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = _('popular car')
        verbose_name_plural = _('popular cars')
