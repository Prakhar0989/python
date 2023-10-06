from django.shortcuts import render
from django.shortcuts import redirect  
# from django.urls import reverse
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

# Create your views here

class UserRegistrationView(APIView):
    def get(self, request):
        return render(request, 'registration_form.html')  # Render the registration form template


    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         username = serializer.validated_data['username']

    #          # Check if the user already exists
    #         if User.objects.filter(username=username).exists():
    #             return Response({'message': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    #         # Create a user with the validated data
    #         user = User.objects.create_user(
    #             username=serializer.validated_data['username'],
    #             password=serializer.validated_data['password'],
    #             email=serializer.validated_data['email']
    #         )
    #          # Redirect to the login page upon successful registration
    #         #login_url = reverse('login')  # Get the URL for the login page
    #         #return redirect(login_url)    

    #         return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
    #     # print(user,"ppppppppppp")
    #     return Response({
    #         'errors': serializer.errors,
    #         'message': 'User registration failed. Please provide valid data.'
    #     }, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def get(self, request):
        return render(request, 'login.html') 

    # def post(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #     if serializer.is_valid():
    #         username = serializer.validated_data.get('username')
    #         password = serializer.validated_data.get('password')

    #         # Authenticate the user
    #         user = authenticate(username=username, password=password)

    #         if user is not None:
    #             # welcome_page_url = reverse('welcome')  
    #             # return  redirect(welcome_page_url)
    #             return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    #         else:

    #             return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# @method_decorator(login_required, name='dispatch')
class WelcomePageView(APIView):
    def get(self, request):
        return render(request, 'welcome_page.html')
    
    def dashboard_get(self, request):
        return render(request, 'dashboard_page.html')