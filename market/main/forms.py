from django import forms
from django.contrib.auth.models import User

from .models import Profile


class ProfileForm(forms.ModelForm):
    ...


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


ProfileFormSet = forms.inlineformset_factory(User, Profile, fields='__all__', extra=0, min_num=1,
                                             can_delete=False)
