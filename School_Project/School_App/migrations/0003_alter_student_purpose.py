# Generated by Django 4.2.3 on 2023-10-07 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School_App', '0002_purpose_alter_student_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='School_App.purpose'),
        ),
    ]