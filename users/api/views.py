from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import FiscalSerializer, RequisitanteSerializer, UserProfileExampleSerializer, XeroxSerializer

from users.models import Fiscal, UserProfileExample, Xerox, Requisitante

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class FiscalViewSet(ModelViewSet):
    serializer_class = FiscalSerializer
    permission_classes = [AllowAny]
    queryset = Fiscal.objects.all()
    http_method_names = ['get', 'put']

class RequisitanteViewSet(ModelViewSet):
    serializer_class = RequisitanteSerializer
    permission_classes = [AllowAny]
    queryset = Requisitante.objects.all()
    http_method_names = ['get', 'put']


class XeroxViewSet(ModelViewSet):
    """ ViewSet para endpoints da Xerox """
    serializer_class = XeroxSerializer
    permission_classes = [AllowAny]
    queryset = Xerox.objects.all()
    http_method_names = ['get', 'put']