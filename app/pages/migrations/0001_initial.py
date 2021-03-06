# Generated by Django 3.1.6 on 2021-02-07 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(max_length=512, upload_to='media/pages/audio/', verbose_name='ссылка на аудио')),
                ('bitrate', models.IntegerField(default=256, help_text='кбит/с', verbose_name='битрейт')),
            ],
            options={
                'verbose_name': 'Аудио',
                'verbose_name_plural': 'Аудио',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1047, verbose_name='название страницы')),
                ('order_number', models.IntegerField(default=1, verbose_name='порядковый номер')),
                ('hide', models.BooleanField(default=False, verbose_name='скрыть')),
                ('counter', models.PositiveIntegerField(default=0, editable=False, verbose_name='счетчик просмотров')),
            ],
            options={
                'verbose_name': 'страница',
                'verbose_name_plural': 'страницы',
                'ordering': ('order_number',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/pages/photo/', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=512, verbose_name='ссылка на видео')),
                ('subtitles', models.CharField(blank=True, max_length=512, null=True, verbose_name='ссылка на субтитры')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1047, verbose_name='название блока контента')),
                ('content_type', models.CharField(choices=[('text', 'текст'), ('audio', 'аудио'), ('video', 'видео'), ('photo', 'фото')], default='text', max_length=10, verbose_name='тип контента')),
                ('order_number', models.PositiveIntegerField(default=1, verbose_name='порядковый номер')),
                ('counter', models.PositiveIntegerField(default=0, editable=False, verbose_name='счетчик просмотров')),
                ('audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='pages.audio', verbose_name='аудио')),
                ('page', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='pages.page', verbose_name='Контент')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='pages.photo', verbose_name='фото')),
                ('text', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='pages.text', verbose_name='текст')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='pages.video', verbose_name='видео')),
            ],
            options={
                'verbose_name': 'контент',
                'verbose_name_plural': 'контент',
                'ordering': ('order_number',),
            },
        ),
    ]
