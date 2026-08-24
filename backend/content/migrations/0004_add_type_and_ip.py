from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('formation', 'Formation'), ('produit', 'Produit digital'), ('service', 'Service')], default='service', max_length=20),
        ),
        migrations.AddField(
            model_name='service',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
