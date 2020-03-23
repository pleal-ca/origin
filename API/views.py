from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from API import models
from API.risk_profile_calculator import calculator

class RiskProfile(APIView):
    def post(self, request, format=None):
        x = request.data
        result = calculator(x)
        return Response(result)
