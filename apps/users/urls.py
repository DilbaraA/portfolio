from apps.users.views import UserRegistrationView
from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView
)
from rest_framework.routers import DefaultRouter as DR

urlpatterns = [
    path('registration/', UserRegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

router= DR()


urlpatterns += router.urls