from django.contrib import admin

from movies.models import Movie
from movies.models import TypeMovie
from movies.models import JobTitle
from movies.models import Artist
from movies.models import Genre
from movies.models import Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','year_of_release']
    filter_horizontal = ['directors','actors','genres']
@admin.register(TypeMovie)
class TypeMovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['id','job_title','description']
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','date_of_birth']
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass    