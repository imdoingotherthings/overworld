from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('igdb', 'name', 'slug', 'cover_id', 'backdrop_id')
