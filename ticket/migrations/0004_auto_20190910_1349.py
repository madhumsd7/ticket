# Generated by Django 2.0.13 on 2019-09-10 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assinged_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticket.Agent'),
        ),
    ]