# Generated by Django 3.0.5 on 2020-04-03 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0004_remove_bills_bill_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labreport',
            name='report_no',
        ),
    ]
