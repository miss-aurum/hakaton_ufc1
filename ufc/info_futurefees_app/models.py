from django.db import models
from app_ufc.models import *


class FutureFees (models.Model):
    sportman = models.ForeignKey(Sportman, on_delete=models.CASCADE)
    turnir = models.ManyToManyField(Turnir, verbose_name='Турнир')
    image = models.ImageField(verbose_name='', upload_to='photoFutureFees/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Будущий сбор'
        verbose_name_plural = 'Будущие сборы'

    def __str__(self) -> str:
        return self.turnir


class PastFees(models.Model):
    turnir = models.ForeignKey(Turnir, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Прошедший сбор'
        verbose_name_plural = 'Прошедшие сборы'



    def __str__(self) -> str:
        return self.turnir
    






            
