from django.db import models
from datetime import datetime
from players.models import Player


FREQUENCY_CHOICES = (
    ('fortnightly', 'Fortnightly'),
    ('monthly', 'Monthly')
)

STATUS_CHOICES = (
    ('active', 'Active'),
    ('ended', 'Ended'),
    ('failed', 'Failed')
)

INVITATION_STATUS = (('accepted', 'Accepted'), ('pending',
                     'Pending'), ('declined', 'Declined'))


class Game(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    frequency = models.CharField(
        max_length=11, choices=FREQUENCY_CHOICES, default='fortnightly')
    duration = models.DecimalField(max_digits=2, decimal_places=0)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=6, choices=STATUS_CHOICES, default='active')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    invitation_status = models.CharField(
        max_length=20, choices=INVITATION_STATUS, default='pending')

    # Use below if you want to stop having same player twice on the same game.
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['game', 'player'], name='unique_game_player_combincation')
    #     ]

    def __str__(self):
        return f"{self.player.user.first_name}'s invitation to {self.game.name} is {self.invitation_status}"
