# Generated by Django 4.0.4 on 2022-05-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_wing_alter_userreport_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wing',
            field=models.CharField(blank=True, choices=[('INFORMATION TECHNOLOGY', 'INFORMATION TECHNOLOGY'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('CIVIL ENGINEERING', 'CIVIL ENGINEERING'), ('TEXTILE ENGINEERING', 'TEXTILE ENGINEERING'), ('TRAVEL`S AND TOURISM', 'TRAVEL`S AND TOURISM'), ('PACKAGING ENGINEERING', 'PACKAGING ENGINEERING'), ('MECHANICAL ENGINEERING', 'MECHANICAL ENGINEERING'), ('ELECTRICAL ENGINEERING', 'ELECTRICAL ENGINEERING'), ('AUTOMOBILE ENGINEERING', 'AUTOMOBILE ENGINEERING'), ('METALLURGICAL ENGINEERING', 'METALLURGICAL ENGINEERING'), ('MINING AND MINE SURVEYING', 'MINING AND MINE SURVEYING'), ('ELECTRONICS AND TELECOMMUNICATION', 'ELECTRONICS AND TELECOMMUNICATION')], max_length=40),
        ),
    ]
