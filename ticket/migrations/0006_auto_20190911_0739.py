# Generated by Django 2.0.13 on 2019-09-11 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20190910_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assinged_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticket.Agent'),
        ),
    ]
