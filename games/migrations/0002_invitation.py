# Generated by Django 4.1 on 2022-08-08 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_status', models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'Pending'), ('declined', 'Declined')], default='pending', max_length=20)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.player')),
            ],
        ),
    ]