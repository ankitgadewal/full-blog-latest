# Generated by Django 3.0.5 on 2020-05-10 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20200503_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='premium',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('charge', models.IntegerField(default=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
