from django.urls import path
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view()),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]