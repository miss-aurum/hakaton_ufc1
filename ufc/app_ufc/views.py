from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets




class SportmanViewset(viewsets.ModelViewSet):
    queryset = Sportman.objects.all()
    serializer_class = SportmanSerializer

class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializers_class = TrainerSerializer

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializers_class = NewsSerializer

class  SocialMediaViewset(viewsets.ModelViewSet):
    queryset =  SocialMedia.objects.all()
    serializers_class = SocialMediaSerializer

class ContactViewset(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializers_class = SocialMediaSerializer

class TurnirViewset(viewsets.ModelViewSet):
    queryset = Turnir.objects.all()
    serializers_class = TurnirSerializer

class PeopleTurnirViewset(viewsets.ModelViewSet):
    queryset = PeopleTurnir.objects.all()
    serializers_class = PeopleTurnirSerializer





  










