from django.db import models

class Platform(models.TextChoices):
    PS1 = "PlayStation 1"
    PS2 = "PlayStation 2"
    PS3 = "PlayStation 3"
    PS4 = "PlayStation 4"
    PS5 = "PlayStation 5"
    PC = "Steam"

class PlayingStatus(models.TextChoices):
    BACK = "Backlogged"
    PLAY = "Playing"
    DONE = "Finished"

class CompletionStatus(models.TextChoices):
    STORY = "Storyline"
    TROPHY = "Trophy Hunting"
    BEYOND = "Achieving 100%"
    COMPLETE = "Completed"

class Game(models.Model):
    game_name = models.CharField(max_length=40)
    original_platform = models.CharField(max_length=13, choices=Platform.choices, default=Platform.PC)
    remastered_platform = models.CharField(max_length=13, choices=Platform.choices, null=True, blank=True, default='null')
    playing_status = models.CharField(max_length=15, choices=PlayingStatus.choices, default=PlayingStatus.PLAY)
    completion_status = models.CharField(max_length=15, choices=CompletionStatus.choices, default=CompletionStatus.STORY)
    platinum = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    hours_played = models.IntegerField()
    single_player = models.BooleanField(default=True)
    game_image_path = models.ImageField(upload_to='game_images/', blank=True, null=True) 
    def __str__(self):
        return self.game_name