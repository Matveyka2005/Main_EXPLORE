from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True, default="photos/default.jpg")
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True, null=True)
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано:")
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return self.title    

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def get_absolute_update_url(self):
        return reverse("update", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')
    # slug = models.SlugField(max_length=50, verbose_name='URL', unique=True, null=True)

    def get_absolute_url(self):
        return reverse('by_rubric', kwargs={'rubric_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class UserProfileUploads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Bb, on_delete=models.CASCADE)


