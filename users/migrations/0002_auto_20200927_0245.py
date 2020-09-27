# Generated by Django 3.0.8 on 2020-09-27 02:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbluser',
            name='Gender',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tbluser',
            name='Phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]