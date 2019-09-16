# Generated by Django 2.0.13 on 2019-09-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('SUPERVISOR', 'SUPERVISOR'), ('ACCOUNT MANAGER', 'ACCOUNT MANAGER')], max_length=20)),
            ],
        ),
    ]
