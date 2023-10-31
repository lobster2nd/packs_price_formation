from rest_framework import serializers

from .models import PurchasePlanningAnalysisData


class PurchasePlanningAnalysisDataSerializer(serializers.ModelSerializer):
    """Сериализатор для модели данных PurchasePlanningAnalysisData"""
    class Meta:
        model = PurchasePlanningAnalysisData
        fields = '__all__'
