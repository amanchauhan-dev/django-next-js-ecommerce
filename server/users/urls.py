from django.urls import path
from .views import (
    BuyerRegisterView,
    BuyerProfileView,
    BuyerTokenObtainPairView,
    BuyerTokenRefreshView,
    BuyerLogoutView
)

urlpatterns = [
    path('buyers/register/', BuyerRegisterView.as_view(), name='buyer-register'),
    path('buyers/login/', BuyerTokenObtainPairView.as_view(), name='buyer-token-obtain'),
    path('buyers/refresh/', BuyerTokenRefreshView.as_view(), name='buyer-token-refresh'),
    path('buyers/profile/', BuyerProfileView.as_view(), name='buyer-profile'),
    path('buyers/logout/', BuyerLogoutView.as_view(), name='buyer-logout'),
]
