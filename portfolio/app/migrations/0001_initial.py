# Generated by Django 4.1.2 on 2022-10-27 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='about')),
                ('title', models.CharField(max_length=20)),
                ('qoute', models.TextField()),
                ('birth', models.CharField(max_length=20)),
                ('website', models.URLField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=50)),
                ('emailadd', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
                ('current', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('links', models.TextField(default='#')),
                ('description', models.TextField()),
                ('authorname', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('dates', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exppoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=30)),
                ('p2', models.CharField(max_length=30)),
                ('p3', models.CharField(max_length=30)),
                ('p4', models.CharField(max_length=30)),
                ('p5', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('imgclass', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('percent', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('dates', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.exppoints')),
            ],
        ),
    ]
