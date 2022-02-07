# Generated by Django 2.2.10 on 2022-02-07 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveys', '0002_auto_20181212_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.CharField(blank=True, help_text='if Type Field is (radio, select, multi select), fill in the option separated by commas. ex: Male, Female', max_length=200, null=True),
        ),
    ]