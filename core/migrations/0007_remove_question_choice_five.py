# Generated by Django 2.2.7 on 2019-11-07 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_question_choice_five'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_five',
        ),
    ]