from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):

    game_id = serializers.ReadOnlyField(source='id') 
    created_time = serializers.ReadOnlyField() 
    updated_time = serializers.ReadOnlyField() 
    class Meta:
        model = Game
        fields = ['game_id','game_name','game_platform','game_status','game_completion_percentage',
                  'hours_played','game_completed','game_image_path',
                  'created_time','updated_time']