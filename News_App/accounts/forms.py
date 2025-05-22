# accounts/forms.py
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=(
            "username",
            "email",
            "age",
            # Dont mention password as it is already included by default
        )
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=(
            "username",
            "email",
            "age",
            # Dont mention password as it is already included by default
        )