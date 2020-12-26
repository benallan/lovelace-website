# Generated by Django 3.1.4 on 2020-12-26 14:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    replaces = [('users', '0001_initial'), ('users', '0002_expanded_user_profiles'), ('users', '0003_fixed_default_avatar_link'), ('users', '0004_added_user_country_field'), ('users', '0005_blank_birthday_and_country_ok'), ('users', '0006_about_and_location_can_be_blank'), ('users', '0007_fixed_default_avatar_filepath'), ('users', '0008_fixed_default_avatar_filepath_v2'), ('users', '0009_fixed_default_avatar_filepath_v3'), ('users', '0010_count_user_problems_solved_and_submissions_made'), ('users', '0011_validators_and_help_text_for_user_model'), ('users', '0012_added_date_format_help_text'), ('users', '0013_fixed_default_avatar_filepath_v4'), ('users', '0014_fixed_default_avatar_filepath_v5'), ('users', '0015_subscribe_to_email_option'), ('users', '0016_remove_userprofile_avatar')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(default='', help_text='Minimum and maximum length of 3-40 characters.', max_length=40, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(40)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('about', models.CharField(blank=True, help_text='Maximum length of 1000 characters.', max_length=1000, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('birthday', models.DateField(blank=True, help_text='Date format: YYYY-MM-DD.', null=True)),
                ('location', models.CharField(blank=True, help_text='Maximum length of 50 characters.', max_length=50, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('problems_solved', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('submissions_made', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('subscribe_to_emails', models.BooleanField(default=True, help_text='Subscribe to emails.')),
            ],
        ),
    ]
