# Generated by Django 4.1.2 on 2023-10-17 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('forum_app', '0009_alter_answer_options_remove_answer_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
