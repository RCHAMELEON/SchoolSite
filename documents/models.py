from django.db import models

class Document(models.Model):
    DOCUMENT_TYPES = (
        ('Education', 'Образование'),
        ('Testimonies', 'Свидетельства'),
        ('Treaty', 'Договоры'),
        ('Regulations', 'Правила'),
        ('Локальные акты', 'Локальные акты'),
        ('Varification', 'Акты проверки'),
        ('Schedule', 'Расписания'),
        ('Standarts', 'Стандарты'),
        ('Safety', 'Безопасность'),
    )

    title = models.CharField(
        max_length = 150,
        verbose_name = "Название документа",
        blank = False,
    )
    desctiption = models.TextField(
        verbose_name = "Описание",
        blank = True,
    )
    document_type = models.CharField(
        verbose_name = "Тип документа",
        blank = False,
        max_length = 50,
        choices = DOCUMENT_TYPES,
    )
    fiel = models.FileField(
        verbose_name = "Файл",
        upload_to = "documents/%Y/%m",
        blank = True,
    )
    tags = models.CharField(
        verbose_name = "Ключевые слова",
        max_length = 150,
        blank = True,
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/documents/list"
