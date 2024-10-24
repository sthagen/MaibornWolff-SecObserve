# Generated by Django 5.1.2 on 2024-10-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rules", "0013_rule_origin_kubernetes_qualified_resource"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rule",
            name="new_severity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Unknown", "Unknown"),
                    ("None", "None"),
                    ("Low", "Low"),
                    ("Medium", "Medium"),
                    ("High", "High"),
                    ("Critical", "Critical"),
                ],
                max_length=12,
            ),
        ),
    ]