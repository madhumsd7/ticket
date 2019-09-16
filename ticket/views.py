# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .pagination import userLimitOffsetPagination
from .pagination import userPageNumberPagination


from .models import Ticket, user, Agent 
from .serializers import TicketSerializer, userSerializer, AgentSerializer


class userList(generics.ListAPIView):
    queryset=user.objects.all()
    serializer_class= userSerializer
    pagination_class = userPageNumberPagination
        
    def get(self,request):
        user1 = user.objects.all().order_by('id')
        serializer = userSerializer(user1 , many = True)
        return Response(serializer.data)
        
    def post(self,request):
        data = request.data
        serializer = userSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status = 400)
        
class userDetails(APIView):
    def get_object(self,id):
        try:
           return user.objects.get(id=id)
        except user.DoesNotExist as e:
           return Respose( {"error" : "not found"}, status=404)

    def get(self,request,id=None):
        instance = self.get_object(id)
        serializer = userSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = userSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.erros,status=400)

    def delete(self,request,id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=204)

class TicketList(APIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def get(self,request):
        Ticket1 = Ticket.objects.all()
        serializer = TicketSerializer(Ticket1 , many = True)
        return Response(serializer.data)
    
    def post(self,request):
        data = request.data
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status = 400)

class TicketDetails(APIView):
    def get_object(self,uuid):
        try:
           return Ticket.objects.get(uuid=uuid.UUID)
        except Ticket.DoesNotExist as e:
           return Respose( {"error" : "not found"}, status=404)

    def get(self,request,id=None):
        record = self.get_object(uuid.UUID)
        serializer = TicketSerializer(record)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = TicketSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros)

    def delete(self,request,id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse()


class AgentList(APIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    
    def get(self,request):
        Agent1 = Agent.objects.all()
        serializer = AgentSerializer(Agent1 , many = True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = AgentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status = 400)

class AgentDetails(APIView):
    def get_object(self,id):
        try:
           return Agent.objects.get(id=id)
        except user.DoesNotExist as e:
           return Respose( {"error" : "not found"}, status=404)

    def get(self,request,id=None):
        instance = self.get_object(id)
        serializer = AgentSerializer(instance)
        return Response(serializer.data)
 
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = agentSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros)

    def delete(self,request,id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse()
