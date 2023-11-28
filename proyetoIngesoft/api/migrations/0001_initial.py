# Generated by Django 4.2.6 on 2023-10-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
                ('ip_configuration', models.CharField(db_column='IP_Configuration', max_length=255)),
                ('ip_uv4_adress', models.CharField(db_column='IP_UV4_Adress', max_length=255)),
                ('subnetmask', models.CharField(db_column='SubnetMask', max_length=255)),
                ('defaultgateway', models.CharField(db_column='DefaultGateway', max_length=255)),
                ('dnsserver', models.CharField(db_column='DNSServer', max_length=255)),
            ],
            options={
                'db_table': 'dispositivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Firewall',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
            ],
            options={
                'db_table': 'firewall',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
                ('port_status', models.IntegerField(db_column='Port Status')),
                ('ipv4_address', models.CharField(db_column='IPv4 Address', max_length=255)),
                ('subnet_mask', models.CharField(db_column='Subnet Mask', max_length=255)),
            ],
            options={
                'db_table': 'interfaces',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InterfacesRouter',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
                ('port_status', models.IntegerField(db_column='Port Status')),
                ('ipv4_adress', models.CharField(db_column='IPv4 Adress', max_length=255)),
                ('subnet_mask', models.CharField(db_column='Subnet Mask', max_length=255)),
            ],
            options={
                'db_table': 'interfaces_router',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
            ],
            options={
                'db_table': 'router',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Switches',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=255)),
            ],
            options={
                'db_table': 'switches',
                'managed': False,
            },
        ),
    ]
