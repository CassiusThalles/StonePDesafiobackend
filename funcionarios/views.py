from rest_framework import decorators
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import FuncionarioSerializer
from .models import Funcionario

class FuncionariosViewSet(ModelViewSet):
    serializer_class = FuncionarioSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        idade = self.request.query_params.get('idade', None)
        cargo = self.request.query_params.get('cargo', None)
        queryset = Funcionario.objects.all()
        if id:
            queryset = Funcionario.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if idade:
            queryset = queryset.filter(idade=idade)
        if cargo:
            queryset = queryset.filter(cargo=cargo)
        return queryset
