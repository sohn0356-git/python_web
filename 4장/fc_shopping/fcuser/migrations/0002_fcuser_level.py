# Generated by Django 3.0.3 on 2020-03-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('admin', '관리자'), ('user', '사용자')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]
