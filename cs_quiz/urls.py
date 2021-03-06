from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cs_quiz.apps.users.urls')),
    path('accounts/', include('allauth.urls')),
    path('quiz/', include('cs_quiz.apps.quiz.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]