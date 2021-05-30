from django.shortcuts import render
from rest_framework.views import APIView
from .models import Profile
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class CreateProfile(APIView):
    
    def post(self,request):
        try:
            with transaction.atomic():
                if User.objects.filter(username=request.data["email"]).count() > 0:
                    return Response(
                        {
                            "status": "Error",
                            "msg": "User Already Registered",
                            "status_code": status.HTTP_409_CONFLICT,
                        }
                    )
                obj = {}
                obj["first_name"] = request.data["first_name"]
                obj["last_name"] = request.data["last_name"]
                obj["email"] = request.data["email"]
                if "image" in request.data:
                        obj["image"] = request.data["image"]
                obj["address_1"] = request.data["address_1"]
                obj["address_2"] = request.data["address_2"]
                obj["pin_code"] = request.data["pin_code"]
                password = request.data["password"]
                u = User(
                    username=request.data["email"], password=password, is_staff=False
                )
                u.save()
                p = Profile(**obj)
                p.save()
                return Response(
                    {
                        "status": "Success",
                        "status_code": status.HTTP_200_OK,
                    }
                )
        except Exception as e:
            return Response(
                {
                    "status": "Error",
                    "msg": str(e),
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                }
            )


        
