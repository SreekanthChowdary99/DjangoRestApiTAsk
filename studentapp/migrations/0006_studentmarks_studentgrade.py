# Generated by Django 3.2.6 on 2021-08-19 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_alter_studentgrades_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmarks',
            name='studentgrade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.studentgrades'),
        ),
    ]
