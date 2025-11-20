from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

class TypeMovie(models.Model):
    title = models.TextField("Название")
    description = models.TextField("Описание")
    class Meta:
        verbose_name = "Тип произведения"
        verbose_name_plural = "Типы произведений"
    def __str__(self) -> str:
        return self.title
class JobTitle(models.Model):
    job_title = models.TextField("Должность")
    description = models.TextField("Описание")
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
    def __str__(self) -> str:
        return self.job_title    
class Artist(models.Model):
    full_name = models.TextField("ФИО")
    date_of_birth  = models.DateField("Дата рождения")
    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"
    def __str__(self) -> str:
        return self.full_name
class Genre(models.Model):
    title = models.TextField("Название")
    description = models.TextField("Описание")
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    def __str__(self) -> str:
        return self.title
class Movie(models.Model):
    title = models.TextField("Название")
    year_of_release = models.PositiveIntegerField("Год выхода", validators=[MinValueValidator(1895), MaxValueValidator(datetime.now().year)])
    type_movie = models.ForeignKey('TypeMovie', on_delete = models.CASCADE,verbose_name='Тип произведения', null = True)
    directors = models.ManyToManyField(Artist, related_name = 'movies+',verbose_name="Режиссеры")
    actors = models.ManyToManyField(Artist, related_name = 'movies+',verbose_name="Актеры")
    genres = models.ManyToManyField(Genre, related_name = 'movies+',verbose_name="Жанры")
    class Meta:
        verbose_name = "Кино"
        verbose_name_plural = "Кино"
class Review(models.Model):
    title = models.TextField("Название")
    text_review = models.TextField("Текст")
    rating = models.PositiveIntegerField("Оценка", validators=[MinValueValidator(1), MaxValueValidator(10)])
    movie = models.ForeignKey('Movie', on_delete = models.CASCADE, verbose_name = "Название произведения", null = True)
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"  

