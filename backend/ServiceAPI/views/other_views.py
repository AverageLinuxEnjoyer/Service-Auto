from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..service.undo_redo_service import UndoRedoService
from ..service.search import full_text_search

from ..serializers.card_serializer import CardSerializer
from ..serializers.car_serializer import CarSerializer


@api_view(['POST'])
def undo(request):
    return Response(UndoRedoService.undo())


@api_view(['POST'])
def redo(request):
    return Response(UndoRedoService.redo())


@api_view(['GET'])
def search(request):
    text = request.GET.get("text", "")

    cars, cards = full_text_search(text)

    car_serializer = CarSerializer(cars, many=True)
    card_serializer = CardSerializer(cards, many=True)

    car_data = car_serializer.data
    card_data = card_serializer.data

    if cars.count() == 0:
        car_data = [
            {
                "id": 0,
                "model": None,
                "acquisition_date": None,
                "kilometers": None,
                "warranty": None,
                "total_workmanship": None
            }
        ]

    if cards.count() == 0:
        card_data = [
            {
                "id": 0,
                "first_name": None,
                "last_name": None,
                "cnp": None,
                "birthday": None,
                "registration_date": None,
                "total_discounts": None
            }
        ]

    return Response({
        "cars": car_data,
        "cards": card_data
    })
