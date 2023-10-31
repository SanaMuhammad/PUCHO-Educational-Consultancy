# Generated by Django 4.0.6 on 2022-08-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_text',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='student',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Feedback_text',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]