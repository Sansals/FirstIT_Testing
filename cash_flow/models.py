from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=64, unique=True)


    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


    def __str__(self):
        return self.name


class TxType(models.Model):
    name = models.CharField(max_length=64, unique=True)


    class Meta:
        verbose_name = 'Тип операции'
        verbose_name_plural = 'Типы операций'


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    tx_type = models.ForeignKey(TxType, on_delete=models.CASCADE, related_name='categories')


    class Meta:
        unique_together = ('name', 'tx_type') # задаём уникальные пары полей
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return f"{self.name} ({self.tx_type})"


class SubCategory(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')


    class Meta:
        unique_together = ('name', 'category') # задаём уникальные пары полей
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


    def __str__(self):
        return f"{self.name} ({self.category})"


class CashFlow(models.Model):
    #Модель ДДС
    created_at = models.DateField(default=timezone.localdate) # можно править вручную, от auto_now_add отказываемся для отображения поля в админке
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    tx_type = models.ForeignKey(TxType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)


    class Meta:
        verbose_name = 'Финансовая операция'
        verbose_name_plural = 'Финансовые операции'
        ordering = ['-created_at', '-id']


    def __str__(self):
        return f"{self.created_at} | {self.tx_type} | {self.category} / {self.subcategory} | {self.amount}"

    def clean(self):
        errors = {}

        if self.amount is None or self.amount == 0:
            errors['amount'] = 'Сумма должна быть больше 0.'

        # Категория должнаа относиться к выбранному типу
        if self.category and self.tx_type:
            if self.category.tx_type_id != self.tx_type_id:
                errors['category'] = 'Выбранная категория не относится к выбранному типу.'

        # подкатегория должна относиться к выбранной категории
        if self.subcategory and self.category:
            if self.subcategory.category_id != self.category_id:
                errors['subcategory'] = 'Выбранная подкатегория не относится к выбранной категории.'

        if errors:
            raise ValidationError(errors)
