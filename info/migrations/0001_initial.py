# Generated by Django 2.2.6 on 2019-12-13 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=25, null=True)),
                ('level', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('background', models.CharField(blank=True, max_length=30, null=True)),
                ('faction', models.CharField(blank=True, max_length=30, null=True)),
                ('race', models.CharField(blank=True, max_length=25, null=True)),
                ('alignment', models.CharField(blank=True, max_length=25, null=True)),
                ('exp_points', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('dci_number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('personality_traits', models.CharField(blank=True, max_length=80, null=True)),
                ('ideals', models.CharField(blank=True, max_length=80, null=True)),
                ('bonds', models.CharField(blank=True, max_length=80, null=True)),
                ('flaws', models.CharField(blank=True, max_length=80, null=True)),
                ('background_story', models.CharField(blank=True, max_length=2500, null=True)),
                ('oth_prof_lan', models.CharField(blank=True, max_length=2000, null=True)),
                ('appearance', models.CharField(blank=True, max_length=250, null=True)),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
