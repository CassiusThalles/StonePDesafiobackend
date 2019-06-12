from rest_framework.serializers import ModelSerializer
from .models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'idade', 'cargo']