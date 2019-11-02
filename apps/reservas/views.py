from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, decorators, pagination
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication
)

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *


class ShortResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class TipoCanchaViewSet(viewsets.ModelViewSet):
    queryset = TipoCancha.objects.all()
    serializer_class = TipoCanchaSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication,)


class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication,)


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication,)
    pagination_class = ShortResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'cancha',
        'fecha_reserva',
        'fecha_turno',
        'hora_turno',
        'id',
        'cliente',
        'empleado'
    ]

    def perform_create(self, serializer):
        serializer.save(empleado=self.request.user)


class OnlyPOST(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
