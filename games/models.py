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
    game_platform = models.CharField(max_length=15, choices=GamePlatform.choices, default=GamePlatform.PC)
    game_status = models.CharField(max_length=11, choices=GameStatus.choices, default=GameStatus.PLAYING)
    game_completion_percentage = models.PositiveIntegerField()
    hours_played = models.PositiveIntegerField()
    game_completed = models.BooleanField(default=False)
    game_image_path = models.ImageField(upload_to='game_images/', blank=True, null=True) 
    created_time = models.DateTimeField(auto_now_add=True)  # Set only on creation
    updated_time = models.DateTimeField(auto_now=True)      # Set on each save

    #class Meta():
    #     unique_together = ('game_name', 'game_platform')