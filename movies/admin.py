from django.contrib import admin

from movies.models import Movie
from movies.models import TypeMovie
from movies.models import JobTitle
from movies.models import Artist
from movies.models import Genre
from movies.models import Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
@admin.register(TypeMovie)
class TypeMovieAdmin(admin.ModelAdmin):
    pass
@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    pass
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass    