# Generated by Django 3.0.7 on 2020-07-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0005_auto_20200702_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='job',
            field=models.CharField(choices=[('Manager', 'Manager'), ('user', 'user')], default='user', max_length=50),
        ),
    ]