# Generated by Django 4.0 on 2021-12-24 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_remove_club_logo'),
        ('event', '0003_alter_eventenrollment_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_events', to='club.club'),
        ),
    ]
