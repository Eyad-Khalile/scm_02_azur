# Generated by Django 3.1.1 on 2020-12-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0004_auto_20201202_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgprofile',
            name='staff',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
