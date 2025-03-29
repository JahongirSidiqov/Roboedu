from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabar'}),
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Tastiqlovchi parol'})
    )
    is_student = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    is_instructor = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "is_student", "is_instructor"]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("is_student") and cleaned_data.get("is_instructor"):
            raise forms.ValidationError("Foydalanuvchi faqat bitta rolni tanlashi mumkin.")
        return cleaned_data
