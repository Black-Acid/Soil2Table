from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


from .serializers import ConsumerSignUpSerializer
from .models import UserModel






class ConsumerSignUP(APIView):
    def post(self, request):
        print(request.data)
        return Response("Message Recieved successfuly")

# the consumer's signup

class SignUp(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ConsumerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response("User saved SUccessfully", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def get(self, request):
        users = UserModel.objects.all()
        serializer = ConsumerSignUpSerializer(users, many=True)
        return Response(serializer.data)