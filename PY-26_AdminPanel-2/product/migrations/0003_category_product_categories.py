# Generated by Django 4.2.2 on 2023-06-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_description_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='product.category'),
        ),
    ]
