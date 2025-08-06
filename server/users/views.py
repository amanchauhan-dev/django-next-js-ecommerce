from rest_framework import generics, permissions
from .serializers import BuyerRegisterSerializer, UserSerializer
from .permissions import IsBuyer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import BuyerTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

User = get_user_model()

class BuyerRegisterView(generics.CreateAPIView):
    serializer_class = BuyerRegisterSerializer
    permission_classes = [permissions.AllowAny]

class BuyerProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsBuyer]
    
    def get_object(self):
        return self.request.user


class BuyerTokenObtainPairView(TokenObtainPairView):
    serializer_class = BuyerTokenObtainPairSerializer

class BuyerTokenRefreshView(TokenRefreshView):
    # uses default serializer
    pass


class BuyerLogoutView(APIView):
    permission_classes = [IsBuyer]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"detail": "Refresh token required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_205_RESET_CONTENT)