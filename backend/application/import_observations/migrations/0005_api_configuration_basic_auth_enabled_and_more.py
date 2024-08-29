# Generated by Django 5.0.7 on 2024-08-02 07:59

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("import_observations", "0004_zap_rename"),
    ]

    operations = [
        migrations.AddField(
            model_name="api_configuration",
            name="basic_auth_enabled",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="api_configuration",
            name="basic_auth_password",
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True),
        ),
        migrations.AddField(
            model_name="api_configuration",
            name="basic_auth_username",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="api_configuration",
            name="query",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="api_configuration",
            name="verify_ssl",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="api_configuration",
            name="api_key",
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True),
        ),
        migrations.AlterField(
            model_name="api_configuration",
            name="project_key",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]