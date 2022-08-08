from datetime import datetime
from django.db import models
from games.models import Game
from players.models import Player


class Payout(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    term = models.DecimalField(max_digits=2, decimal_places=0)
    date = models.DateField(default=datetime.now)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player.user.first_name}'s payout date is {self.date} and amount is {self.amount}"
