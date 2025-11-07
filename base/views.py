from django.shortcuts import render, redirect
from .forms import BaseForm

def create_user(request):
    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirigez vers une page de succès ou une autre page de votre choix
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = BaseForm()
        return render(request, 'register.html', {'form': form})