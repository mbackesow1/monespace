# Generated by Django 3.2.6 on 2023-08-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_changed_my_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='entreprise',
            field=models.CharField(choices=[('ccbm', 'ccbm'), ('orbit', 'orbit')], default='entreprise', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='postu',
            field=models.CharField(default='post', max_length=128, null=True, verbose_name='Poste'),
        ),
        migrations.AlterField(
            model_name='users',
            name='sectu',
            field=models.CharField(default='secteur', max_length=128, null=True, verbose_name='Secteur'),
        ),
    ]
