from rest_framework import serializers
from .models import user
from .models import Ticket 
from .models import Agent

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = '__all__'
        paginate_by = 1


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('user',
                  'priority',
                  'link',
                  'description',
                  'assinged_to',
                  'history',
                  'created_by'
                   )

class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'