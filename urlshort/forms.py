from .models import ShortURL
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# expiration time choices
EXPIRATION_CHOICES = [
    ('', 'Never'),
    ('1', '1 Hour'),
    ('24', '1 Day'),
    ('168', '1 Week'),
    ('720', '1 Month'),
]

class CreateNewShortURL(forms.ModelForm):
    # optional custom short code
    custom_code = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Leave empty for random code'
        })
    )
    
    # expiration time dropdown
    expiration = forms.ChoiceField(
        choices=EXPIRATION_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    class Meta:
        model = ShortURL
        fields = ['original_url']

        widgets = {
            'original_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your long URL here...'
            })
        }

# form for editing the original url        
class EditURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url']
        
        widgets = {
            'original_url': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

# signup form - extends django's built in UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # add bootstrap classes to the form fields
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'