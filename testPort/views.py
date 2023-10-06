from django.shortcuts import render
# from django.shortcuts import redirect  
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.response import Response
from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from testPort.serializers import UserSerializer
# from testPort.serializers import LoginSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here

class UserRegistrationView(APIView):
    def get(self, request):
        return render(request, 'registration_form.html')  # Render the registration form template

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html') 
    

class Pages(APIView):
    def get(self, request, page_type):
        if page_type == 'register':
            return render(request, 'registration.html')
        elif page_type == 'login':
            return render(request, 'login.html')
        elif page_type == 'welcome':
            return render(request,'welcome.html')
        else :
            return render('invalid page ')


# @method_decorator(login_required, name='dispatch')     
class Welcome(APIView):
    def get(self, request):
        return render(request, 'welcome.html')