# Generated by Django 3.2.6 on 2021-08-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0007_alter_hebword_partofspeech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hebword',
            name='transliteration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]