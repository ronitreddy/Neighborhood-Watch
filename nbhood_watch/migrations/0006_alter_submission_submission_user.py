# Generated by Django 4.2.10 on 2024-02-25 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nbhood_watch', '0005_alter_submission_submission_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nbhood_watch.user', verbose_name='Submission User'),
        ),
    ]