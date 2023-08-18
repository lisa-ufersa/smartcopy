from rest_framework import serializers
from users.models import Fiscal, Requisitante, UserProfileExample, Xerox

class UserProfileExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']

class FiscalSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    class Meta:
        model = Fiscal
        fields = ['id', 'matricula', 'unidade', 'first_name', 'data_vinculo', 'user']

    def get_first_name(self, obj):
        return obj.user.first_name
    
class RequisitanteSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    class Meta:
        model = Requisitante
        fields = ['id', 'matricula', 'first_name']

    def get_first_name(self, obj):
        return obj.user.first_name

class XeroxSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Xerox
        fields = ['id', 'unidade', 'cnpj','first_name']
    
    def get_first_name(self, obj):
        return obj.user.first_name