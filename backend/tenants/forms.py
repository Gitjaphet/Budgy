from django import forms

class InscriptionForm(forms.Form):
    nom_organisation = forms.CharField(
        max_length=100,
        label="Nom de l'organisation",
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex: Minjara',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'contact@minjara.com',
            'class': 'form-control'
        })
    )
    telephone = forms.CharField(
        max_length=20,
        label="Numéro de téléphone",
        widget=forms.TextInput(attrs={
            'placeholder': '+261 34 00 000 00',
            'class': 'form-control'
        })
    )
    mot_de_passe = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'form-control'
        })
    )
    mot_de_passe_confirm = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'form-control'
        })
    )

    def clean_nom_organisation(self):
        nom = self.cleaned_data['nom_organisation'].lower().strip()
        nom = ''.join(c for c in nom if c.isalnum())
        if len(nom) < 3:
            raise forms.ValidationError("Le nom doit contenir au moins 3 caractères alphanumériques.")
        return nom

    def clean(self):
        cleaned_data = super().clean()
        mdp = cleaned_data.get('mot_de_passe')
        mdp_confirm = cleaned_data.get('mot_de_passe_confirm')
        if mdp and mdp_confirm and mdp != mdp_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data
    

class FindTenantForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'votre@email.com',
            'class': 'form-control',
            'autofocus': True
        })
    )