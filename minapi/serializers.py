from rest_framework import serializers
from . models import Stores,Recipe

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stores
        fields= (
            'id',
            'name',
            'after_discount_flour',
            'after_discount_rice',
            'after_discount_eggs',
            'after_discount_sugar',
            'after_discount_salt',
            'after_discount_vegetables',
        )

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'