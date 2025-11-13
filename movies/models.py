from django.db import models

class TypeMovie(models.Model):
    title = models.TextField("Название")
    description = models.TextField("Описание")
    class Meta:
        verbose_name = "Тип произведения"
        verbose_name_plural = "Типы произведений"
class JobTitle(models.Model):
    job_title = models.TextField("Должность")
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
class Artist(models.Model):
    full_name = models.TextField("ФИО")
    date_of_birth  = models.DateField("Дата рождения")
    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"
class Genre(models.Model):
    genre_title = models.TextField("Название")
    description = models.TextField("Описание")
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
class Movie(models.Model):
    title = models.TextField("Название")
    year_of_release = models.TextField("Год выхода")
    type_movie = models.ForeignKey(TypeMovie, on_delete = models.CASCADE, name = "Тип произведения")
    directors = models.ManyToManyField(Artist, related_name = 'movies+')
    actors = models.ManyToManyField(Artist, related_name = 'movies+')
    genres = models.ManyToManyField(Genre, related_name = 'movies+')
    class Meta:
        verbose_name = "Кино"
        verbose_name_plural = "Кино"
class Review(models.Model):
    title = models.TextField("Название")
    text_review = models.TextField("Текст")
    rating = models.IntegerField("Оценка")
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, name = "Название произведения")
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"  

