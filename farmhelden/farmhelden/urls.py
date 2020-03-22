from django.urls import include, path
from rest_framework import routers
from rest_server.views import FarmViewSet, CampaignViewSet, LocationViewSet, RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'campaigns', CampaignViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('auth', RegistrationAPIView.as_view()),
    path('auth/sign_in', LoginAPIView.as_view()),
    path('auth/user', UserRetrieveUpdateAPIView.as_view()),
    path('', include(router.urls)),
]
