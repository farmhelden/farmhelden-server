from django.urls import include, path
from rest_framework import routers
from rest_server.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('auth', RegistrationAPIView.as_view()),
    path('auth/sign_in', LoginAPIView.as_view()),
    path('auth/user', UserRetrieveUpdateAPIView.as_view()),
]
