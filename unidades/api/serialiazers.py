from rest_framework import serializers

from unidades.models import Impressao, Maquina, Unidade

class MaquinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maquina
        fields = '__all__'

class UnidadeSerializer(serializers.ModelSerializer):
    responsavel = serializers.SerializerMethodField()
    maquina = serializers.SerializerMethodField()

    class Meta:
        model = Unidade
        fields = ['id','local','responsavel','maquina']
    
    def get_responsavel(self, obj):
        return obj.xerox.user.first_name
    
    def get_maquina(self, obj):
        return obj.maquina.modelo

class ImpressaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Impressao
        fields = ['id', 'data_solicitada', 'data_impressa', 'data_entregue', 'maquina', 'qnt', 'arquivo', 'colordo']