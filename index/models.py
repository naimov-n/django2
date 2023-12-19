from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/", blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = "Новости"


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    status = models.BooleanField(default=True, verbose_name="Статус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категория"


class Social(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    icon = models.CharField(max_length=255, verbose_name="Иконка")
    link = models.CharField(max_length=255, verbose_name="Ссылка", blank=True)
    status = models.BooleanField(default=True, verbose_name="Статус")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = "Социальные сети"