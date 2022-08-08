# Generated by Django 4.1 on 2022-08-08 12:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0002_invitation'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.DecimalField(decimal_places=0, max_digits=2)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='games.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.player')),
            ],
        ),
    ]
