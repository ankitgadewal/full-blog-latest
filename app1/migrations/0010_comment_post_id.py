# Generated by Django 3.0.7 on 2020-07-10 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.Post'),
            preserve_default=False,
        ),
    ]
