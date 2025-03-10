from album.forms import AlbumModelForm, BandModelForm, GenreModelForm
from album.models import Band, Album, Genre
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'bd'

    def get_queryset(self):
        albums = super().get_queryset().order_by('-id')
        search = self.request.GET.get('search')

        if search:
            albums = albums.filter(album__icontains=search)
        return albums

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['bands'] = Band.objects.all()
        
        return context


class AlbumInfoView(DetailView):
    model = Album
    template_name = 'album_info.html'


class BandsView(ListView):
    model = Band
    template_name = 'bands.html'
    context_object_name = 'bd'

    def get_queryset(self):
        band = super().get_queryset().order_by('name')

        return band
    

class GenresView(ListView):
    model = Album
    template_name = 'genres.html'
    context_object_name = 'bd'

    def get_queryset(self):
        genre = super().get_queryset().order_by('genre').distinct('genre')

        return genre
    

class BandInfoView(DetailView):
    model = Band
    template_name = 'band_info.html'


class GenreAlbumsView(ListView):
    model = Genre
    template_name = 'genre_albums.html'
    context_object_name = 'bd'

    def get_queryset(self):
        genre = super().get_queryset().filter(genre='Heavy Metal')

        return genre


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewAlbumCreateView(CreateView):
    model = Album
    form_class = AlbumModelForm
    template_name = 'new_album.html'
    success_url = '/home'


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumModelForm
    template_name = 'album_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('album_info', kwargs={'pk': self.object.pk})
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = '/home'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewBandCreateView(CreateView):
    model = Band
    form_class = BandModelForm
    template_name = 'new_band.html'
    success_url = '/bands'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewGenreCreateView(CreateView):
    model = Genre
    form_class = GenreModelForm
    template_name = 'new_genre.html'
    success_url = '/genres'
