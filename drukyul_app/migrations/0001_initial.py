# Generated by Django 3.1.6 on 2021-03-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(upload_to='profiles')),
                ('introduction', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Adviser Table',
            },
        ),
        migrations.CreateModel(
            name='BhutanPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'BhutanPage Table',
            },
        ),
        migrations.CreateModel(
            name='Blog_CommuniteeStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'Blog CommuniteeStory Table',
            },
        ),
        migrations.CreateModel(
            name='BreathingBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'BreathingBook Table',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact Table',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(upload_to='profiles')),
                ('introduction', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Director Table',
            },
        ),
        migrations.CreateModel(
            name='DrukyulSalon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'DrukyulSalon Table',
            },
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('published_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Initiative Table',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='LockdownRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'LockdownRead Table',
            },
        ),
        migrations.CreateModel(
            name='News_Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'News_Update Table',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(upload_to='profiles')),
                ('introduction', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Producer Table',
            },
        ),
        migrations.CreateModel(
            name='Sponsor_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='Sponsor_Partner')),
                ('website_link', models.URLField()),
            ],
            options={
                'verbose_name': 'Sponsor_Partner Table',
            },
        ),
        migrations.CreateModel(
            name='StoryTelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_published', models.DateField()),
            ],
            options={
                'verbose_name': 'StoryTelling Table',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('occupation', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Volunteer Table',
            },
        ),
    ]
