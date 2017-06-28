from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class New(models.Model):
    title = models.CharField(
        max_length = 150,
        verbose_name = "Название новости",
        blank = False,
    )
    text = RichTextUploadingField(
        verbose_name = "Содержание новости",
        blank = False,
    )
    preview_picture = models.ImageField(
        upload_to = "images/%Y/%m/%d",
        verbose_name = "Картинка анонса",
        blank = True,
    )
    tags = models.CharField(
        verbose_name = "Ключевые слова",
        max_length = 150,
        blank = True,
    )
    like = models.IntegerField(
        blank = True,
        default = 0,
    )

    def __str__(self):
        return self.title

    def anons_text(self):
        for i in range(len(self.text)):
            if self.text[i] == '.':
                return self.text[:i]+" ..."

    def get_absolute_url(self):
        return '/news/new/%i/' % self.id
