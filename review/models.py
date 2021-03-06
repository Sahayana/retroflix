from django.db import models
from movie.models import Movie
from user.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

# Create your models here.


# STAR_RATE=[(1,1),
#             (2,2),
#             (3,3),
#             (4,4),
#             (5,5),]

def cal_age(birthday):
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age


class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    star = models.IntegerField(default=0)

    def __str__(self):
        return self.author.username

    
  