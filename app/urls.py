from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from album.views import HomeView, AlbumInfoView, BandsView, GenresView, BandInfoView, NewAlbumCreateView, AlbumUpdateView, AlbumDeleteView, NewBandCreateView, NewGenreCreateView
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('album/<int:pk>', AlbumInfoView.as_view(), name='album_info'),
    path('album/<int:pk>/update', AlbumUpdateView.as_view(), name='album_edit'),
    path('album/<int:pk>/delete', AlbumDeleteView.as_view(), name='album_delete'),
    path('bands/', BandsView.as_view(), name='bands'),
    path('genres/', GenresView.as_view(), name='genres'),
    path('bandinfo/<int:pk>', BandInfoView.as_view(), name='band_info'),
    path('new-album/', NewAlbumCreateView.as_view(), name='new_album'),
    path('new-band/', NewBandCreateView.as_view(), name='new_band'),
    path('new-genre/', NewGenreCreateView.as_view(), name='new_genre'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
