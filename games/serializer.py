from rest_framework import serializers
from .models import Game

class GamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id',
                  'game_name',
                  'original_platform',
                  'remastered_platform',
                  'playing_status',
                  'completion_status',
                  'platinum',
                  'completed',
                  'hours_played'
                  ]