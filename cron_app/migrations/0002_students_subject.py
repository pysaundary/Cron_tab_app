# Generated by Django 3.2.5 on 2021-07-14 07:44

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cron_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='subject',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Java', 1), ('Python', 2), ('Ruby', 3), ('C++', 4), ('DotNet', 5), ('Php', 6)], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
