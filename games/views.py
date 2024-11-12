from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Game
from .serializer import GamesSerializer

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        queryset = Game.objects.all()
        serializer = GamesSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GamesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_game_by_id(request, id):
    if request.method == 'GET':
        try:
            account = Game.objects.get(id = id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GamesSerializer(account)
        return Response(serializer.data)
    