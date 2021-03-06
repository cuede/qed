# Generated by Django 2.1 on 2018-08-13 22:51

from django.db import migrations, models
from django.utils.text import slugify


def poner_slug(apps, schema_editor):
    Materia = apps.get_model('enunciados', 'Materia')
    for materia in Materia.objects.all():
        materia.slug = slugify(materia.nombre)
        materia.save()


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0005_auto_20180810_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='slug',
            field=models.SlugField(default='hola', max_length=1023, unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(poner_slug),
    ]
