from django import forms
from .models import Base

class BaseForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = ['user', 'genre', 'email', 'pwd']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Base.objects.filter(email=email).exists():
            raise forms.ValidationError("L'email est déjà utilisé.")
        return email
class EmailForm(forms.Form):
    email = forms.EmailField(label='Entrez votre adresse e-mail')

class PasswordForm(forms.Form):
    new_password = forms.CharField(label='Nouveau mot de passe', widget=forms.PasswordInput)
class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Télécharger une image')
