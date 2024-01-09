# Generated by Django 4.2.5 on 2023-12-20 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.IntegerField()),
                ('spreadsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='que.spreadsheet')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_name', models.TextField()),
                ('spreadsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='que.spreadsheet')),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='que.column')),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='que.row')),
                ('spreadsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='que.spreadsheet')),
            ],
        ),
    ]
