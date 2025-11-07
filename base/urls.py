from django.urls import path
from .views import create_user

urlpatterns = [
    path('register/', create_user, name='register'),
    # Ajoutez une URL pour la page de succès ou une autre page de votre choix
]
