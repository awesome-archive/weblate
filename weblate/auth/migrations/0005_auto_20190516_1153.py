# Generated by Django 2.2 on 2019-05-16 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("weblate_auth", "0004_auto_20180827_1406")]

    operations = [
        migrations.AlterModelOptions(
            name="autogroup",
            options={
                "verbose_name": "Automatic group assignment",
                "verbose_name_plural": "Automatic group assignments",
            },
        ),
        migrations.AlterModelOptions(
            name="permission",
            options={
                "verbose_name": "Permission",
                "verbose_name_plural": "Permissions",
            },
        ),
    ]