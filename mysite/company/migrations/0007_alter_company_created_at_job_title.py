# Generated by Django 5.0 on 2024-12-18 21:49

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_company_created_at_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime(2024, 12, 18, 21, 49, 21, 232425)),
        ),
        migrations.CreateModel(
            name='job_title',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=200)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.dept')),
            ],
        ),
    ]
