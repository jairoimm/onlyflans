from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label='Nombre:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese nombre aquí'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese correo aquí'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje:',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3 fst-italic',
            'rows': 5,
            'placeholder': 'Ingrese mensaje. Máximo 500 carácteres'
        })
    )
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Usuario:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese el usuario aquí'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese su email aquí'
        })
    )
    password = forms.CharField(
        max_length=50,
        label='Contraseña:',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese la contraseña aquí'
        })
    )
    passRepeat = forms.CharField(
        max_length=50,
        label='Repita la Contraseña:',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Repita la Contraseña aquí'
        })
    )