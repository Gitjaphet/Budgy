from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'votre@email.com',
            'class': 'form-control',
            'autofocus': True
        })
    )
    mot_de_passe = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'form-control'
        })
    )

class FindTenantForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'votre@email.com',
            'class': 'form-control',
            'autofocus': True
        })
    )