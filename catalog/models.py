from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    def __str__(self):
        pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
