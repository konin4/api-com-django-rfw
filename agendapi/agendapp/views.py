from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from agendapp.models import Agenda
from agendapp.serializers import AgendaSerializer
# from django.http import HttpResponse

class AgendaList(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


# def hello(request):
#    text = """<h1>welcome to my app !</h1>"""
#    return HttpResponse(text)
