# Generated by Django 4.1.3 on 2022-12-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='Açıklama')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'ordering': ['-date_time', 'id'],
            },
        ),
    ]
