from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .serializers import UserSerializer
from .models import UserModel




class RegisterUser(APIView):
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User saved successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "your Name": f"{user.username}"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


class FarmerDashboard(APIView):
    pass



class AddNewProducts(APIView):
    def post(self, request):
        pass



class AvailableProducts(APIView):
    def get(self, request):
        pass


class AddNewReview(APIView):
    def post(self, request):
        pass



class FarmerReview(APIView):
    pass


class Transactions(APIView):
    pass




class Orders(APIView):
    pass








class ConsumerSignUP(APIView):
    def post(self, request):
        print(request.data)
        return Response("Message Recieved successfuly")

# the consumer's signup

class SignUp(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response("User saved SUccessfully", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)