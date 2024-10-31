from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializer import GameSerializer




@api_view(['GET','POST','OPTIONS'])
def index(request):
    if request.method == 'GET':
        queryset = Game.objects.all()
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'OPTIONS':
        print("Options Are Here, why is that doing it?")
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_book(request,id):
    if request.method == 'GET':
        try:
            game = Game.objects.get(id = id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game)
        return Response(serializer.data)