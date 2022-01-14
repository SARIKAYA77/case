from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from crud.serializers import DataSerializer
from crud.models import Data

# def index(request):
#     return HttpResponse("TASK STARTED")

class ListDataAPIView(ListAPIView):
    """This endpoint list all of the available datas from the database"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class CreateDataAPIView(CreateAPIView):
    """This endpoint allows for creation of a data"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class UpdateDataAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific data by passing in the id of the data to update"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DeleteDataAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Data from the database"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer