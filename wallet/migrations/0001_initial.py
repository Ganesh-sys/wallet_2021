# Generated by Django 3.2.4 on 2021-06-29 12:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owned_by', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.CharField(blank=True, choices=[('enable', 'Enable'), ('disable', 'Disable')], max_length=64, null=True)),
                ('enabled_at', models.DateTimeField(null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('enable', 'Enable'), ('disable', 'Disable')], max_length=64, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('reference_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deposite_id', to='wallet.wallet')),
                ('withdrawn_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('enable', 'Enable'), ('disable', 'Disable')], max_length=64, null=True)),
                ('deposited_at', models.DateTimeField(null=True)),
                ('enabled_at', models.DateTimeField(null=True)),
                ('amount', models.IntegerField()),
                ('reference_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wallet.wallet')),
            ],
        ),
    ]
