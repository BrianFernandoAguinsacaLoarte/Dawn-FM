from rest_framework import serializers

from dawnbem.models import Registro


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'