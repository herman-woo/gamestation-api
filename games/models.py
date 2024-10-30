from django.db import models

class GameStatus(models.TextChoices):
    BACKLOGGED = "Backlogged"
    WAITLIST = "Waitlist"
    PLAYING = "Playing"
    POST = "Post-Game"
    FINISHED = "Finished"

class GamePlatform(models.TextChoices):
    PS3 = "Playstation 3"
    PS4 = "Playstation 4"
    PS5 = "Playstation 5"
    PC = "Steam"


class Game(models.Model):
    game_name = models.CharField(max_length=100)
    game_platform = models.CharField(max_length=100, choices=GamePlatform.choices, default=GamePlatform.PC)
    game_status = models.CharField(max_length=100, choices=GameStatus.choices, default=GameStatus.PLAYING)
    game_completion_percentage = models.IntegerField()
    hours_played = models.IntegerField()
    game_completed = models.BooleanField()
    game_image_path = models.CharField(max_length=250)
    created_time = models.DateTimeField(null=True,auto_now_add=True)  # Set only on creation
    updated_time = models.DateTimeField(null=True, auto_now=True)      # Set on each save
