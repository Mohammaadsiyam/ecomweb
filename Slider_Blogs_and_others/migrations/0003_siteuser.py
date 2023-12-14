# Generated by Django 4.1.2 on 2022-11-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider_Blogs_and_others', '0002_alter_blog_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siteuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default=None, max_length=100)),
                ('First_Name', models.CharField(default=None, max_length=30)),
                ('Last_Name', models.CharField(default=None, max_length=30)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=11)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]