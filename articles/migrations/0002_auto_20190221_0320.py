# Generated by Django 2.1.5 on 2019-02-21 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Article', 'verbose_name_plural': 'Blog Articles'},
        ),
    ]
