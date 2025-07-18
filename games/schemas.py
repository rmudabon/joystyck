from ninja import ModelSchema, Schema
from .models import Game

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = ['id', 'name', 'platform', 'date_added', 'genre', 'status']

class GameCreateSchema(ModelSchema):
    class Meta:
        model = Game
        fields = ['name', 'platform', 'genre', 'status']
