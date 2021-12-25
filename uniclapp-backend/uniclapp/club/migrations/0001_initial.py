# Generated by Django 4.0 on 2021-12-25 00:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('rate', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('category', models.CharField(choices=[('business', 'Business'), ('entertainment', 'Entertainment'), ('sport', 'Sport'), ('policy', 'Policy')], max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ClubFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='club.club')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followees', to='accounts.student')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
