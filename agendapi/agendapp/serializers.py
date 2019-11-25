from rest_framework import serializers
from .models import Agenda
# from django.contrib.auth.models import Agenda

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  
        model = Agenda
        fields = '__all__'

