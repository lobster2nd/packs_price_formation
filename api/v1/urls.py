from django.urls import path

from .views import ElementListAPIView, ElementRetrieveUpdateDestroyAPIView, \
    ElementCreateAPIView

urlpatterns = [
    path('elements/', ElementListAPIView.as_view()),
    path('elements/create/', ElementCreateAPIView.as_view()),
    path('elements/<int:pk>/', ElementRetrieveUpdateDestroyAPIView.as_view()),
]
