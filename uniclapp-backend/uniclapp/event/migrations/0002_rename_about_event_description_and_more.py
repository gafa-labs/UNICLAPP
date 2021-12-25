# Generated by Django 4.0 on 2021-12-25 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='about',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='building',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='eventenrollment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_events', to='event.event'),
        ),
        migrations.AlterField(
            model_name='eventenrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_students', to='accounts.student'),
        ),
    ]
