from django.db import models

NULLABLE = {'null': True, 'blank': True}
class Post(models.Model):
   title = models.CharField(max_length=150, verbose_name='заголовок')
   body = models.TextField(verbose_name='содержимое')
   slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
   photo = models.ImageField(upload_to='post/', **NULLABLE, verbose_name='превью')
   created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
   is_published = models.BooleanField(default=True, verbose_name='признак публикации')
   views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

   def __str__(self):
       return self.title

   class Meta:
       verbose_name = 'статья'
       verbose_name_plural = 'статьи'