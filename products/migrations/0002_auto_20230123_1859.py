# Generated by Django 3.2 on 2023-01-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pt_sessions',
            options={'verbose_name_plural': 'Pt_sessions'},
        ),
        migrations.AlterModelOptions(
            name='subscriptions',
            options={'verbose_name_plural': 'Subscriptions'},
        ),
        migrations.RemoveField(
            model_name='pt_sessions',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subscriptions',
            name='user',
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='include_1',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='include_2',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='include_3',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]