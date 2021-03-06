# Generated by Django 3.2.7 on 2021-09-27 10:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('manager_name', models.CharField(blank=True, max_length=100)),
                ('manager_number', models.CharField(blank=True, max_length=20)),
                ('manager_email', models.EmailField(blank=True, max_length=254)),
                ('hospital_name', models.CharField(blank=True, max_length=100)),
                ('hospital_number', models.CharField(blank=True, max_length=20)),
                ('hospital_email', models.EmailField(blank=True, max_length=254)),
                ('police_name', models.CharField(blank=True, max_length=100)),
                ('police_number', models.CharField(blank=True, max_length=20)),
                ('police_email', models.EmailField(blank=True, max_length=254)),
                ('hood_pic', cloudinary.models.CloudinaryField(default='image/upload/v1627343010/neighborhood1_cj2fyx.jpg', max_length=255, verbose_name='images')),
            ],
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=50)),
                ('phase', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('profile_picture', cloudinary.models.CloudinaryField(default='image/upload/v1626430054/default_zogkvr.png', max_length=255, verbose_name='images')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.gender')),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='neighbors', to='hood.neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.neighborhood')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.posttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='hood.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('start_day', models.CharField(max_length=50)),
                ('end_day', models.CharField(max_length=50)),
                ('open_time', models.CharField(max_length=50)),
                ('close_time', models.CharField(max_length=50)),
                ('bs_image', cloudinary.models.CloudinaryField(default='image/upload/v1627341811/company_default_qb4ili.png', max_length=255, verbose_name='images')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.profile')),
            ],
        ),
    ]
