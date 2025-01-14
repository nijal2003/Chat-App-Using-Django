# Generated by Django 3.2.7 on 2023-01-30 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20230130_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', blank=True, length=20, max_length=25, null=True, prefix='')),
                ('full_name', models.CharField(max_length=1000)),
                ('bio', models.CharField(default='I am an investor', max_length=100)),
                ('country', models.CharField(default='My Country', max_length=100, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='user_images')),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.CharField(default='+123 (456) 789', max_length=100)),
                ('website', models.URLField(blank=True, default='https://stridearn.com/', null=True)),
                ('pin', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=20, prefix='', unique=True)),
                ('facebook', models.URLField(blank=True, default='https://facebook.com/', null=True)),
                ('instagram', models.URLField(blank=True, default='https://instagram.com/', null=True)),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/', null=True)),
                ('whatsApp', models.CharField(blank=True, default='+123 (456) 789', max_length=100, null=True)),
                ('level_1', models.BooleanField(default=False)),
                ('level_2', models.BooleanField(default=False)),
                ('level_3', models.BooleanField(default=False)),
                ('level_4', models.BooleanField(default=False)),
                ('level_5', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('code', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890abcdefghij', length=10, max_length=20, prefix='REF', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ref_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
