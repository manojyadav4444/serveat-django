# Generated by Django 3.2.3 on 2021-05-29 14:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics')),
                ('number_of_ratings', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(max_length=30)),
                ('pin_code', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
