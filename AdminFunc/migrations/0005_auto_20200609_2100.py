# Generated by Django 3.0.5 on 2020-06-09 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AdminFunc', '0004_auto_20200606_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=3)),
                ('added_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]