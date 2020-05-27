# Generated by Django 3.0.3 on 2020-05-26 15:35

from django.db import migrations


def create_stokens(apps, schema_editor):
    Stoken = apps.get_model('django_etesync', 'Stoken')
    CollectionItemRevision = apps.get_model('django_etesync', 'CollectionItemRevision')

    for rev in CollectionItemRevision.objects.all():
        rev.stoken = Stoken.objects.create()
        rev.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_etesync', '0008_auto_20200526_1535'),
    ]

    operations = [
        migrations.RunPython(create_stokens),
    ]