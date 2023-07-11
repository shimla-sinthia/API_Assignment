from django.db import models

Size = (
    ('Tiny', 'Tiny'),
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)

Intensity = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
Gender = (
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others'),
)

class Breed(models.Model):
    


    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255, choices=Size)
    friendliness = models.IntegerField(choices=Intensity)
    trainability = models.IntegerField(choices=Intensity)
    shedding_amount = models.IntegerField(choices=Intensity)
    exercise_needs = models.IntegerField(choices=Intensity)

    def __str__(self):
        return self.name


class Dog(models.Model):
    
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', related_name= 'dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=30,choices=Gender)
    color = models.CharField(max_length=30)
    favourite_food = models.CharField(max_length=255)
    favourite_toy = models.CharField(max_length=255)

    def __str__(self):
        return self.name