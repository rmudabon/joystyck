from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .schemas import GameSchema, GameCreateSchema
from .models import Game
from typing import List

api = NinjaAPI()
# Create your views here.

@api.get('/games', response=List[GameSchema])
def list_games(request):
    games = Game.objects.all()
    return games

@api.post('/games')
def create_game(request, payload: GameCreateSchema):
    new_game = Game.objects.create(**payload.dict())
    return {"id": new_game.id}

@api.get('/games/{game_id}', response=GameSchema)
def get_game(request, game_id: int):
    game = get_object_or_404(Game, id=game_id)
    return game

@api.put('/games/{game_id}', response=GameSchema)
def update_game(request, game_id: int, payload: GameCreateSchema):
    game = get_object_or_404(Game, id=game_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(game, attr, value)
    game.save()
    return { "success": True }

@api.delete('/games/{game_id}')
def delete_game(request, game_id: int):
    game = get_object_or_404(Game, id=game_id)
    game.delete()
    return { "success": True }
