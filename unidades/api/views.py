from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from unidades.api.serialiazers import ImpressaoSerializer, MaquinaSerializer, UnidadeSerializer
from unidades.models import Impressao, Maquina, Unidade

class UnidadeViewSet(ModelViewSet):
    serializer_class = UnidadeSerializer
    permission_classes = [AllowAny]
    queryset = Unidade.objects.all()
    # http_method_names = ['get', 'put']

class MaquinaViewSet(ModelViewSet):
    serializer_class = MaquinaSerializer
    permission_classes = [AllowAny]
    queryset = Maquina.objects.all()
    # http_method_names = ['get', 'put']

class ImpressaoViewSet(ModelViewSet):
    serializer_class = ImpressaoSerializer
    permission_classes = [AllowAny]
    queryset = Impressao.objects.all()