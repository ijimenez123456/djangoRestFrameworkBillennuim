from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
]