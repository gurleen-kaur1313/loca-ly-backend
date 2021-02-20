# Generated by Django 3.1.7 on 2021-02-20 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pgs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usertype', models.CharField(blank=True, choices=[('B', 'BOYS'), ('G', 'GIRLS'), ('O', 'BOTH')], max_length=250, null=True)),
                ('roomtype', models.CharField(blank=True, choices=[('1', 'SINGLE SEATER'), ('2', 'DOUBLE SEATER'), ('3', 'THREE SEATER')], max_length=250, null=True)),
                ('kitchen_available', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=250, null=True)),
                ('washroom_attached', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=250, null=True)),
                ('laundry_included', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=250, null=True)),
                ('rent', models.IntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.location')),
            ],
        ),
    ]
