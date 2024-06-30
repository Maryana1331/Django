from django.db import models
from django.urls import reverse_lazy

# verbose_name перевод поля на русский
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('View_news', kwargs={'pk': self.pk})
    #Описание моделей в админке
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        # сортировка
        ordering = ['-created_at']


class Category(models.Model):

    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')


    def get_absolute_url(self):
        return reverse_lazy('Category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # сортировка по полю title
        ordering = ['title']
