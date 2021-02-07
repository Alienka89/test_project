from django.core.exceptions import ValidationError
from django.db import models
from django.db import transaction


class Text(models.Model):
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f'{self.id} {self.text[:80]}'

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class Audio(models.Model):
    audio = models.FileField(max_length=512, verbose_name='ссылка на аудио', upload_to='media/pages/audio/')
    bitrate = models.IntegerField(default=256, help_text='кбит/с', verbose_name='битрейт')

    def __str__(self):
        return f'{self.id} {self.audio} {self.bitrate}'

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'


class Video(models.Model):
    video = models.CharField(max_length=512, verbose_name='ссылка на видео')
    subtitles = models.CharField(max_length=512, verbose_name='ссылка на субтитры', null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.video}'

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Photo(models.Model):
    photo = models.ImageField(verbose_name='изображение', upload_to='media/pages/photo/')

    def __str__(self):
        return f'{self.id} {self.photo}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Page(models.Model):
    title = models.CharField(verbose_name='название страницы', max_length=1047)
    order_number = models.IntegerField(default=1, verbose_name='порядковый номер')
    hide = models.BooleanField(default=False, verbose_name='скрыть')
    counter = models.PositiveIntegerField(default=0, verbose_name='счетчик просмотров', editable=False)

    def __str__(self):
        return self.title

    @transaction.atomic
    def update_counter(self):
        self.counter += 1
        self.save()
        for i in self.content.all():
            i.update_counter()

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'


class Content(models.Model):
    TYPE_CHOICES = (
        ('text', 'текст'),
        ('audio', 'аудио'),
        ('video', 'видео'),
        ('photo', 'фото'),
    )
    DICT_TYPE_CHOICES = dict(TYPE_CHOICES)
    title = models.CharField(verbose_name='название блока контента', max_length=1047)
    content_type = models.CharField(verbose_name='тип контента', default=TYPE_CHOICES[0][0], choices=TYPE_CHOICES,
                                    max_length=10)
    order_number = models.PositiveIntegerField(default=1, verbose_name='порядковый номер')
    counter = models.PositiveIntegerField(default=0, verbose_name='счетчик просмотров', editable=False)

    page = models.ForeignKey(Page, default=None, null=True, verbose_name='Контент', related_name='content',
                             on_delete=models.CASCADE)

    photo = models.ForeignKey(Photo, verbose_name=DICT_TYPE_CHOICES['photo'], related_name='content', null=True,
                              blank=True, on_delete=models.SET_NULL)
    text = models.ForeignKey(Text, verbose_name=DICT_TYPE_CHOICES['text'], related_name='content', null=True,
                             blank=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, verbose_name=DICT_TYPE_CHOICES['video'], related_name='content', null=True,
                              blank=True, on_delete=models.SET_NULL)
    audio = models.ForeignKey(Audio, verbose_name=DICT_TYPE_CHOICES['audio'], related_name='content', null=True,
                              blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} [{self.DICT_TYPE_CHOICES[self.content_type]}]'

    def update_counter(self):
        self.counter += 1
        self.save()

    def clean(self):
        validation_errors = {}
        content_type = self.content_type
        if not getattr(self, content_type):
            validation_errors[
                content_type] = f"Заполните поле {self.DICT_TYPE_CHOICES[content_type]} или смените тип контента"
        if validation_errors:
            raise ValidationError(message=validation_errors)

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'контент'
        verbose_name_plural = 'контент'
