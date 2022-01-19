from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)
from crud.serializers import DataSerializer
from crud.paginations import DataPagination
from crud.models import Data
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin
import requests
from django.shortcuts import redirect


def Train(request):
    response = requests.get("http://127.0.0.1:5000/train")
    return HttpResponse(response.text)


@receiver(request_finished)
def get_request(sender, **kwargs):
    print("reqeust finished")


def Prediction(request, text):
    response = requests.get("http://127.0.0.1:5000/prediction/" + text)
    return HttpResponse(response.text)


class ListDataAPIView(ListAPIView):
    """This endpoint list all of the available datas from the database"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    pagination_class = DataPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['text', 'label']


class CreateDataAPIView(CreateAPIView):
    """This endpoint allows for creation of a data"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class UpdateDataAPIView(UpdateAPIView, DestroyModelMixin, RetrieveModelMixin):
    """This endpoint allows for updating a specific data by passing in the id of the data to update and allows for deletion of a specific Data from the database and update the database"""
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# class DeleteDataAPIView(DestroyAPIView):
#     """This endpoint allows for deletion of a specific Data from the database"""
#     queryset = Data.objects.all()
#     serializer_class = DataSerializer

# class DeleteDataAPIView(DestroyAPIView,UpdateModelMixin,RetrieveModelMixin):
#     queryset = Data.objects.all()
#     serializer_class = DataSerializer
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
