# Generated by Django 3.2.7 on 2023-01-28 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_gallery_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-date'], 'verbose_name_plural': '2. Category'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-date'], 'verbose_name_plural': '3. Service'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '1. Users'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='phone',
        ),
    ]
