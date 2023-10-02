from typing import Any
from django.utils.timezone import now
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()

class LastVisitMiddleware():
    def __init__(self,get_responece):
        self.get_responce = get_responece
    def __call__(self,request):
        user = request.user
        if not user.is_anonymous:
            User.objects.filter(id = user.id).update(last_login = now())
        
        print("before")
        responce = self.get_responce(request)
        print("after")
        return responce





        

