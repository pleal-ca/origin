from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from API import models
from API.risk_profile_calculator import riskcalculator

class RiskProfile(APIView):
    def post(self, request, format=None):
        aux = request.data
        try:
            result = riskcalculator(aux)
        except:
            return Response('Error: Invalid Content', status=status.HTTP_400_BAD_REQUEST)
        return Response(result)

#   A checagem de erro testa apenas casos de inputs de tipagem incorreta,
#   ex: age = "bom dia". Não foram testados inputs fora dos limites dados
#   pelo assignment, ex: age = -10.
