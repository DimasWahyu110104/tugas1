# Generated by Django 4.2.6 on 2023-11-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_kontak'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=255)),
                ('No_Hp', models.IntegerField()),
                ('Email', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Kontak',
        ),
    ]
