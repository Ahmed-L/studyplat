# Generated by Django 3.2.4 on 2021-06-04 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cat_choices', models.CharField(choices=[('IGSE', 'IGCSE'), ('IAL', 'IAL')], max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('video', models.CharField(blank=True, max_length=300)),
                ('chapter_num', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.subject')),
            ],
        ),
    ]