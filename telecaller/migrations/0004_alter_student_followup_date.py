# Generated by Django 4.0.1 on 2022-01-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecaller', '0003_student_telecaller_alter_student_enquiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='followup_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]