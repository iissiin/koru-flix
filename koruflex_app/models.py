from django.db import models
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField('Название категории', max_length = 255)
    slug = models.SlugField(unique = True, editable = False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Film(models.Model):
    title = models.CharField("Название фильма", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    year = models.CharField("Год выпуска", max_length=100, default="")
    film = models.CharField('Видео', max_length=255, default="")
    director = models.CharField("Режиссер", max_length=255, default="")
    description = models.TextField("Описание фильма ", default="")
    promoPhoto = models.ImageField("Фото", upload_to="images/promo/", default="")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title


class History(models.Model):
    title = models.CharField('Заголовок - продолжить просмтор', max_length=255)
    description = models.TextField('Описание фильма')
    video = models.CharField('Видео', max_length=255, default="")
    yearRelese = models.CharField('Год выауска', max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию", default="")
    promoPhoto = models.ImageField("Фото", upload_to="images/histories/", default="")

    class Meta:
        verbose_name = "Просмотренное"
        verbose_name_plural = "Просмотренные"

    def _str_(self):
        return self.title
