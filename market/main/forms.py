from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        attrs = {
            'class': 'form-control',
            'style': 'width:10%',
        }

        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(attrs)
        self.fields['username'].widget.attrs.update({'readonly': True})
        self.fields['first_name'].widget.attrs.update(attrs)
        self.fields['last_name'].widget.attrs.update(attrs)
        self.fields['email'].widget.attrs.update(attrs)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        help_texts = {
            'username': None
        }


ProfileFormSet = forms.inlineformset_factory(User, Profile, fields=('birth_date',), extra=0, min_num=1,
                                             can_delete=False,
                                             widgets={
                                                 'birth_date': forms.DateInput(attrs={
                                                     'type': 'date',
                                                     'class': 'form-control',
                                                     'style': 'width:10%',
                                                 }),
                                             })
