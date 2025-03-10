from django import forms
from album.models import Album, Band, Genre


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class BandModelForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class GenreModelForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
