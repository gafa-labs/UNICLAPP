# Generated by Django 4.0 on 2021-12-23 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
        ('accounts', '0001_initial'),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.TextField(choices=[('business', 'Business'), ('entertainment', 'Entertainment'), ('sport', 'Sport'), ('policy', 'Policy')])),
                ('status', models.TextField(choices=[('draft', 'Draft'), ('active', 'Active'), ('past', 'Past'), ('upcoming', 'Upcoming'), ('rejected', 'Rejected')])),
                ('about', models.TextField()),
                ('ge_status', models.BooleanField(default=False)),
                ('ge_point', models.IntegerField(default='10')),
                ('duration', models.FloatField(default=0)),
                ('capacity', models.IntegerField(default=0)),
                ('is_online', models.BooleanField(default=False)),
                ('zoom_link', models.URLField(blank=True)),
                ('date', models.DateTimeField()),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='place.building')),
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_events', to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='EventEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_events', to='event.event')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_students', to='accounts.student')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]