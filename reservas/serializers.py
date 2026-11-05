from rest_framework import serializers
from .models import Reserva, Alocacao, PetAlocado


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = [
            "id",
            "proprietario",
            "data_entrada",
            "data_saida",
            "status",
            "criado_em",
        ]

        read_only_fields = ["id", "criado_em"]

    def validate(self, dados):
        data_entrada = dados.get(
            "data_entrada",
            getattr(self.instance, "data_entrada", None)
        )

        data_saida = dados.get(
            "data_saida",
            getattr(self.instance, "data_saida", None)
        )

        if data_entrada and data_saida:
            if data_saida <= data_entrada:
                raise serializers.ValidationError({
                    "data_saida": "A data de saída deve ser posterior à data de entrada."
                })

        return dados



class AlocacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alocacao
        fields = [
            "id",
            "reserva",
            "canil",
            "valor_diaria",
        ]



class PetAlocadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetAlocado
        fields = [
            "id",
            "alocacao",
            "pet",
        ]
