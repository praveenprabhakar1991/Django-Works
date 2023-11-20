# Generated by Django 4.2.5 on 2023-10-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=69)),
                ('Category', models.CharField(default='', max_length=69)),
                ('SubCategory', models.CharField(default='', max_length=69)),
                ('Price', models.IntegerField(default='0')),
                ('Descriptions', models.CharField(default='', max_length=333)),
                ('Publish_date', models.DateField(default='', verbose_name='timezone.now')),
                ('Image', models.ImageField(default='', upload_to='shop/Images')),
            ],
        ),
    ]
