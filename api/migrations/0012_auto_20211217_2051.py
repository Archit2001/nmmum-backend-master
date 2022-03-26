# Generated by Django 3.2.4 on 2021-12-17 15:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_recent_alternate_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='descripton',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='recent',
            name='alternate_text',
            field=models.CharField(blank=True, default=uuid.UUID('c09a4a30-77ad-4b31-a6fa-a5bd2b8e726d'), max_length=50, null=True),
        ),
    ]
