# Generated by Django 4.2.2 on 2024-03-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите заголовок', max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='Человекопонятный URL')),
                ('content', models.TextField(blank=True, help_text='Добавьте описание', null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, help_text='Приложите фото', null=True, upload_to='blog_images', verbose_name='Изображение (превью)')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('view_counter', models.PositiveIntegerField(default=0, help_text='Укажите кол-во просмотров', verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['created_at', 'is_published', 'view_counter'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите наименование товара', max_length=50, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, help_text='Опишите товар', null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, help_text='Фото товара', null=True, upload_to='prod_images', verbose_name='Изображение (превью)')),
                ('price', models.IntegerField(help_text='Стоимость товара', verbose_name='Цена за покупку')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания (записи в БД)')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Дата последнего изменения (записи в БД)')),
                ('category', models.ForeignKey(blank=True, help_text='Категория товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(help_text='Укажите номер версии', verbose_name='Номер версии')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название версии')),
                ('working_ver', models.BooleanField(blank=True, help_text='Укажите признак текущей версии', null=True, verbose_name='Признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
