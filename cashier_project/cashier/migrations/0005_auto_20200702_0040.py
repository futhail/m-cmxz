# Generated by Django 3.0.7 on 2020-07-01 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0004_auto_20200702_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='branche_id_for',
            field=models.CharField(choices=[('1', 'الفرع الرئيسي'), ('2', 'فرع صعده'), ('3', 'فرع عمران')], default='الرئيسي', max_length=30),
        ),
    ]