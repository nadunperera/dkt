from django.db import models
from games.models import Game
from players.models import Player

INVITATION_STATUS = (('accepted', 'Accepted'), ('pending',
                     'Pending'), ('declined', 'Declined'))


class Invitation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(
        Player, on_delete=models.DO_NOTHING)
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
