from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    DOMAIN = (
        ("INFO", "Сведения"),
        ("EDUC", "Образование"),
        ("GRAD", "Выпускникам"),
        ("STNT", "Образовательные стандарты"),
        ("PSY", "Советы психолога"),
    )
    title = models.CharField(
        max_length = 200,
        verbose_name = "Название",
        blank = False,

    )
    text = RichTextUploadingField(
        verbose_name = "Содержание",
        blank = False,
    )
    domain = models.CharField(
        verbose_name = "Область распространения",
        choices = DOMAIN,
        blank = False,
        max_length = 100,
    )
    image = models.ImageField(
        verbose_name = "Картинка анонса",
        blank = True,
    )
    like = models.IntegerField(
        blank = True,
        default = 0,
    )
    tags = models.CharField(
        verbose_name = "Ключевые слова",
        blank = True,
        max_length = 150,
    )

    def __str__(self):
        return self.title

    def anons_text(self):
        for i in range(len(self.text)):
            if i==100:
                return self.text[:i]+" ..."

    def get_absolute_url(self):
        return "/"
