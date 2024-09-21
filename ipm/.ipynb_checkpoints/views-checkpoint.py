from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ipm.serializers import UsersSerializer
from ipm.models import UsersApi
from rest_framework.views import APIView
from rest_framework.response import Response

import joblib
import numpy as np
from rest_framework import status


class UserCreateListView(generics.ListCreateAPIView):
    queryset = UsersApi.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersApi.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]


model = joblib.load("linear_regression_model.pkl")


class PredictView(APIView):
    def post(self, request):
        try:
            # Extrair dados de entrada do request (exemplo: {'input': [5.1]})
            data = request.data.get("input")

            # Convertendo a entrada em formato adequado para o modelo
            input_data = np.array(data).reshape(1, -1)

            # Fazer predição
            prediction = model.predict(input_data)

            # Retornar o resultado como resposta JSON
            return Response({"prediction": prediction[0]}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
