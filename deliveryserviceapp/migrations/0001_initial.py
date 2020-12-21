# Generated by Django 3.1.3 on 2020-12-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('Tracking_id', models.CharField(blank=True, max_length=200, null=True)),
                ('Deliveryaddress', models.CharField(blank=True, max_length=700, null=True)),
                ('Deliverymethod', models.CharField(blank=True, choices=[('Air', 'Air'), ('Sea', 'Sea'), ('Rail', 'Rail'), ('Road', 'Road')], max_length=200, null=True)),
                ('Deliverystatus', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('Currentlocation', models.CharField(blank=True, max_length=600, null=True)),
                ('Deliverydescription', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]