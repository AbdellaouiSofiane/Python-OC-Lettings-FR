# Generated by Django 3.0 on 2022-10-24 14:25

from django.db import migrations

def transfer_model_records(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    AddressOld = apps.get_model('oc_lettings_site', 'Address')
    Addressnew = apps.get_model('lettings', 'Address')
    for address_old in AddressOld.objects.using(db_alias).all():
        instance_dict = address_old.__dict__
        instance_dict.pop('_state')
        Addressnew.objects.using(db_alias).create(**instance_dict)

    LettingOld = apps.get_model('oc_lettings_site', 'Letting')
    Lettingnew = apps.get_model('lettings', 'Letting')
    for letting_old in LettingOld.objects.using(db_alias).all():
        instance_dict = letting_old.__dict__
        instance_dict.pop('_state')
        Lettingnew.objects.using(db_alias).create(**instance_dict)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial')
    ]

    operations = [
        migrations.RunPython(transfer_model_records, migrations.RunPython.noop)
    ]
