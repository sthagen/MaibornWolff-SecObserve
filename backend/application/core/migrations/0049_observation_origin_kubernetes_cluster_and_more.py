# Generated by Django 5.0.8 on 2024-08-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0048_populate_product_checkboxes"),
        ("import_observations", "0006_parser_alter_api_configuration_parser"),
        ("rules", "0012_alter_rule_parser"),
        ("vex", "0007_alter_csaf_tracking_current_release_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="observation",
            name="origin_kubernetes_cluster",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="observation",
            name="origin_kubernetes_namespace",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="observation",
            name="origin_kubernetes_qualified_resource",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="observation",
            name="origin_kubernetes_resource_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="observation",
            name="origin_kubernetes_resource_type",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="has_kubernetes_resource",
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name="observation",
            index=models.Index(
                fields=["origin_kubernetes_qualified_resource"],
                name="core_observ_origin__656035_idx",
            ),
        ),
    ]