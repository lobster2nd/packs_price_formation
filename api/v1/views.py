from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView,
                                     CreateAPIView)
from rest_framework.pagination import PageNumberPagination

from .models import PurchasePlanningAnalysisData
from .serializers import PurchasePlanningAnalysisDataSerializer


class ElementAPIListPagination(PageNumberPagination):
    """Пагинация результирующего списка"""
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ElementListAPIView(ListAPIView):
    """Просмотр списка всех элементов"""
    queryset = PurchasePlanningAnalysisData.objects.all()
    serializer_class = PurchasePlanningAnalysisDataSerializer
    pagination_class = ElementAPIListPagination


class ElementCreateAPIView(CreateAPIView):
    """Создание нового элемента"""
    queryset = PurchasePlanningAnalysisData.objects.all()
    serializer_class = PurchasePlanningAnalysisDataSerializer


class ElementRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление элемента по индексу"""
    queryset = PurchasePlanningAnalysisData.objects.all()
    serializer_class = PurchasePlanningAnalysisDataSerializer
    lookup_field = 'pk'
