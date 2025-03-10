from django.contrib import admin
from album.models import Band, Genre, Album


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    search_fields = ('genre',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album', 'band_name', 'genre', 'year',)
    search_fields = ('band__name', 'album', 'genre', 'year',)


admin.site.register(Band, BandAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Album, AlbumAdmin)
