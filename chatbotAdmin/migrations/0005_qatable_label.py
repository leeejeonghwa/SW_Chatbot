# Generated by Django 4.2.7 on 2023-11-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotAdmin', '0004_rename_answer_content_qatable_a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qatable',
            name='label',
            field=models.IntegerField(default=0),
        ),
    ]
