from rest_framework import serializers
from .models import *

class SportmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportman
        fields = '__all__'
        
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['__all__']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['__all__']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['__all__']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['__all__']




class TurnirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnir
        fields = ['__all__']

class PeopleTurnirSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleTurnir
        fields = ['__all__']

