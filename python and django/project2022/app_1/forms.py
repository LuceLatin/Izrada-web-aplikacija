from django import forms
from django.forms import ModelForm
from .models import Korisnik, Predmeti, UpisniList
from django.contrib.auth.forms  import UserCreationForm


class KorisnikForm(UserCreationForm):
    class Meta:
        model = Korisnik
        fields = ['username', 'email', 'role', 'status' ]

class KorisnikbezlozinkeForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ['username', 'email', 'role', 'status' ]


class PredmetiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('nositelj_kolegija').queryset = Korisnik.objects.filter(role='profesor')
    class Meta:
        model = Predmeti
        fields = ['name', 'kod', 'program', 'ects', 'sem_red', 'sem_izv', 'izborni', 'nositelj_kolegija']



class UpisniListForm(ModelForm):
    class Meta:
        model = UpisniList
        fields = [ 'student_id', 'predmet_id', 'status'] #'student_id', 'predmet_id', 


class NoviUpisniListForm(ModelForm):
    class Meta:
        model = UpisniList
        fields = [ 'status'] #'student_id', 'predmet_id', 





