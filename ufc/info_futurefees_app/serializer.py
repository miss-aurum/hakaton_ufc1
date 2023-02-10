from rest_framework import serializers
from .models import *

class FutureFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutureFees
        fields = ['__all__']

class PastFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastFees
        fields = ['__all__']