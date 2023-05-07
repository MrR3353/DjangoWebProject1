# Generated by Django 4.2 on 2023-05-01 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20221226_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='ID пользователя')),
                ('product_id', models.IntegerField(verbose_name='ID услуги')),
                ('employer_id', models.IntegerField(verbose_name='ID мастера')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Корзина услуг',
                'verbose_name_plural': 'Корзины услуг',
                'db_table': 'Service_basket',
            },
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 14, 0), verbose_name='Дата записи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='employer_id',
            field=models.IntegerField(default=1, verbose_name='ID мастера'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 1, 13, 20, 3, 180506), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 1, 13, 20, 3, 181475), verbose_name='Дата комментария'),
        ),
    ]
