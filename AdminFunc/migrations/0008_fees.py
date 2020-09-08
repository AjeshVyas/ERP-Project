# Generated by Django 3.0.5 on 2020-09-07 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminFunc', '0007_auto_20200713_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('paid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminFunc.Student_Details')),
            ],
        ),
    ]
