from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (ListAPIView, RetrieveUpdateDestroyAPIView,
                                     CreateAPIView)
from rest_framework.pagination import PageNumberPagination

from .models import PurchasePlanningAnalysisData
from .serializers import PurchasePlanningAnalysisDataSerializer


class ElementAPIListPagination(PageNumberPagination):
    """Пагинация результирующего списка"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ElementListAPIView(ListAPIView):
    """Просмотр списка всех элементов"""
    queryset = PurchasePlanningAnalysisData.objects.all()
    serializer_class = PurchasePlanningAnalysisDataSerializer
    pagination_class = ElementAPIListPagination

    @swagger_auto_schema(
        operation_summary='Просмотр списка всех элементов'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ElementCreateAPIView(CreateAPIView):
    """
    Создание нового элемента. Обязательные параметры:
    date_from, date_to, our_warehouse
    """
    queryset = PurchasePlanningAnalysisData.objects.all()
    serializer_class = PurchasePlanningAnalysisDataSerializer

    @swagger_auto_schema(operation_summary='Создание нового элемента')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


RESPONSES = {
            200: PurchasePlanningAnalysisDataSerializer(),
            404: openapi.Response('Запись с таким ID не найдена',
                                  PurchasePlanningAnalysisDataSerializer()),
        }


class ElementRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление элемента по индексу"""
    queryset = PurchasePlanningAnalysisData.objects.all()
    serializer_class = PurchasePlanningAnalysisDataSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(operation_summary='Просмотр элемента по ID',
                         operation_description='Просмотр элемента по ID',
                         responses=RESPONSES)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Редактирование элемента по ID',
                         operation_description='Редактирование элемента по ID',
                         responses=RESPONSES)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Редактирование элемента по ID',
                         operation_description='Редактирование элемента по ID',
                         responses=RESPONSES)
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Удаление элемента по ID',
                         operation_description='Удаление элемента по ID',
                         responses=RESPONSES)
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
