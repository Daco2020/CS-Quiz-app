from django.shortcuts import render
from django.contrib import auth
from rest_framework import views


class SignupView(views.APIView):
    def post(self, request):
        return render(request, 'login.html')

class LoginView(views.APIView):
    def get(self, request):
        return render(request, 'login.html')
    
class LogoutView(views.APIView):
    def post(self, request):
        auth.logout(request)
        return render(request, 'login.html')