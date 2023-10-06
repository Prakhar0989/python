from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth import get_user_model
from django.shortcuts import redirect  
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from testPort.serializers import UserSerializer
from testPort.serializers import LoginSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser, FormParser
# __________________________________________________________________________________________________
# Create your views here

class RegistrationAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            profile_image = request.data.get('profile_image')
            print("aaaaaaaaaaaaaaaaa",profile_image)

            print("Checking for username:", username)
            # if profile_image:
            #     user.profile_image = profile_image
            #     user.save()

             # Check if the user already exists
            User = get_user_model()
            if User.objects.filter(username=username).exists():
                return Response({'message': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)
           
            # Create a user with the validated data
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email']
            ) 
              # Create the associated UserProfile
            profile = UserProfile.objects.create(user=user)
            
            # Save the profile image
            if profile_image:
                profile.profile_image.save(profile_image.name, profile_image)
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response({
            'errors': serializer.errors,
            'message': 'User registration failed. Please provide valid data.'
        }, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            # Authenticate the user
            user = authenticate(username=username, password=password)

            if user is not None:
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)