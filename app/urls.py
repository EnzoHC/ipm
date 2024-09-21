from django.contrib import admin
from django.urls import path
from ipm.views import UserCreateListView, UserRetrieveUpdateDestroyView, PredictView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("api/v1/users", UserCreateListView.as_view(), name="users_create_list"),
    path("api/v1/users/<int:pk>", UserRetrieveUpdateDestroyView.as_view(), name="users_detail_view"),
    path("api/v1/authentication/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/authentication/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/authentication/token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("api/v1/predict", PredictView.as_view(), name="predict"),
]

