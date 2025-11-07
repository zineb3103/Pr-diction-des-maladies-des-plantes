from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse
from base.models import Base
from base.forms import EmailForm, PasswordForm, ImageUploadForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import numpy as np
from PIL import Image
from django.core.files.storage import default_storage
from .model_utils import create_model, predict_image
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_image')
        # else :
        #     return redirect('index')
    return render(request, 'pages/gmail.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        gender = request.POST.get('genre')  

        if not all([username, email, password, gender]):
            return HttpResponse("Tous les champs sont requis.", status=400)

        # Vérifiez si l'e-mail existe dans User ou Base
        if not User.objects.filter(email=email).exists() and not Base.objects.filter(email=email).exists():
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            hashed_password = make_password(password)
            # Ajouter l'utilisateur à la table Base
            base_user = Base.objects.create(
                user=username,
                genre=gender,
                email=email,
                pwd=hashed_password  # Attention à la sécurité des mots de passe
            )
            base_user.save()

            login(request, user)
            return redirect('index')  # Remplacez 'success_page' par la vue ou l'URL de votre choix
        else:
            return HttpResponse("L'email est déjà utilisé.", status=400)

    return render(request, 'pages/register.html')

def forget_password(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                # Redirect to the password reset page
                return redirect('reset_password', email=email)
            except User.DoesNotExist:
                # Redirect to the registration page
                return redirect('register')
    else:
        form = EmailForm()
    return render(request, 'pages/forget_password.html')

def process_image(image_path):
    image = Image.open(image_path)
    image = image.resize((150,150))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Créer ou charger un modèle
model = create_model()

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data['image']
            file_path = default_storage.save(uploaded_image.name, uploaded_image)
            full_path = default_storage.path(file_path)

            # Prédire avec l'image
            prediction = predict_image(model, full_path)
            result = 'Healthy' if prediction[0] < 0.5 else 'Diseased'

            return render(request, 'pages/result.html', {'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'pages/validation.html', {'form': form})
def reset_password(request, email):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            try:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Mot de passe modifié avec succès !')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Utilisateur non trouvé.')
                return redirect('register')
    else:
        form = PasswordForm()
    return render(request, 'pages/reset_password.html', {'form': form, 'email': email})