from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from apps.users.serializer import UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
# from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
User = get_user_model()
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter
# from rest_framework.decorators import action
# from apps.user.email import send_msg

# class UserView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class= UserSerializers

class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None:
            return Response({
                'error': 'user with such username is already exists'
            }, status=400) 
        else:
            user = User.objects.create(
                username = username,
                email = email
            )
            user.set_password(password)
            user.save()
            # send_msg.delay(email)
            return Response(
                {
                    'message':'Success'
                }, status=201
            )
        








    

    