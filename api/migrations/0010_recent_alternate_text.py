# Generated by Django 3.2.4 on 2021-12-17 13:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20211212_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='recent',
            name='alternate_text',
            field=models.CharField(blank=True, default=uuid.UUID('4852bb40-32dd-4b46-8b77-bb4ad01e2825'), max_length=50, null=True),
        ),
    ]