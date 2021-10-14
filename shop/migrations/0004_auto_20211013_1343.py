# Generated by Django 3.2.7 on 2021-10-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300),
        ),
    ]