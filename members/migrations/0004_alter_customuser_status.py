# Generated by Django 4.2.14 on 2024-08-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_customuser_mentor_or_mentee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('', 'Select'), ('mentor', 'Mentor'), ('mentee', 'Mentee')], max_length=6),
        ),
    ]
