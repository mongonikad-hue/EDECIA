from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_add_type_and_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='ip_address',
        ),
    ]
