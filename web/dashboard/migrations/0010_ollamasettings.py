# Generated by Django 3.2.4 on 2024-04-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_delete_openaikeys'),
    ]

    operations = [
        migrations.CreateModel(
            name='OllamaSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('selected_model', models.CharField(max_length=500)),
            ],
        ),
    ]
