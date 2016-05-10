from django import forms
from .models import User


class ExtraDataForm(forms.ModelForm):

    server_choices = (
        ('br', 'BR'), ('eune', 'EUNE'), ('euw','EUW'),  ('jp','JP'),
        ('kr','KR'),  ('lan','LAN'), ('las','LAS'), ('na','NA'), ('oce','OCE'), ('ru','RU'), ('tr','TR')
    )
    server = forms.ChoiceField(choices=server_choices, widget=forms.Select(attrs={'class':'form-control selectpicker', 'required': True}))

    class Meta:
        model = User
        fields = ['summoner_name', 'server']
        widgets = {
            'summoner_name': forms.TextInput(attrs={'placeholder':"SummonerName", 'class':'form-control', 'required': True}),
            }

class SingUpForm(forms.ModelForm):

    server_choices = (
        ('br', 'BR'), ('eune', 'EUNE'), ('euw','EUW'),  ('jp','JP'),
        ('kr','KR'),  ('lan','LAN'), ('las','LAS'), ('na','NA'), ('oce','OCE'), ('ru','RU'), ('tr','TR')
    )
    server = forms.ChoiceField(choices=server_choices, widget=forms.Select(attrs={'class':'form-control selectpicker', 'required': True}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email','summoner_name', 'server']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':"Username", 'required': True}),
            'password': forms.TextInput(attrs={'placeholder':"Password", 'required': True, 'type':'password'}),
            'email': forms.TextInput(attrs={'placeholder':"Email", 'required': True, 'type':'email'}),
            'summoner_name': forms.TextInput(attrs={'placeholder':"SummonerName", 'required': True}),
            }
